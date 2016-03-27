#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
* Monte Carlo Tree Search, 使用UCT算法
* 相连定义为横、竖、对角相邻
* 5子相连胜
* 行棋方4子已相连，并且两端无子，必胜
* 对方已3子相连，并且两端无子，行棋必须下在对方两端
* 当以上情况无出现，优先下在距离本方棋子最近的地方
"""

import math
import random

_debug = True
_debug = False

def debug(*values):
  if _debug:
    log('debug', *values)

def info(*values):
  log('info', *values)

def log(level, *values):
  message = '[%s]' % level
  for value in values:
    message += '\t%s' % str(value)
  print message

board_size = [9, 9]
first_step = [5, 5]
train_num = 1000
#train_num = 1

class Board:
  def __init__(self):
    self.width = self.height = 9
    self.x = self.y = -1
    self.steps = [[-1 for x in range(self.width)] for y in range(self.height)]
    debug(self.steps)

  def check(self, x, y):
    if x < self.width and y < self.height:
      return True
    return False

  def add(self, x, y, c):
    self.x = x
    self.y = y
    debug('x, y', x, y)
    debug(str(self.steps[x][y]))
    self.steps[x][y] = c

  def terminal(self):
    if -1 in self.steps:
      return True

    y_start, y_end = self.compare_list(self.y)
    x_list = self.steps[self.x] [y_start:y_end]
    debug('y_start and y_end: ', y_start, y_end);
    debug('x_list: ' + str(x_list));
    if self.serial(x_list):
      return True

    x_start, x_end = self.compare_list(self.x)
    y_list = map(list, zip(*self.steps))[self.y][x_start:x_end]
    debug('x_start and x_end: ', x_start, x_end);
    debug('y_list: ' + str(y_list));
    if self.serial(y_list):
      return True

    x_start, y_start, x_end, y_end = self.diagonal(self.x, self.y)
    dia_list = []
    while x_start < x_end:
      dia_list.append(self.steps[x_start][y_start])
      x_start += 1
      y_start + 1
    debug('dia_list: ' + str(dia_list));
    if self.serial(dia_list):
      return True

    return False

  def compare_list(self, point):
    start = point - 4
    if start < 0: start = 0
    end = point + 4
    if end > 8: end = 8
    return  start, end

  def diagonal(self, x, y):
    start_x, end_x = self.compare_list(x)
    start_y, end_y = self.compare_list(y)
    # left up
    start_x_count = x - start_x
    start_y_count = y - start_y
    if start_x_count != start_y_count:
      if start_x_count < start_y_count:
	start_y = y - start_x_count
      else:
	start_x = x - start_y_count
    # right down
    end_x_count = end_x - x
    end_y_count = end_y - y
    if end_x_count != end_y_count:
      if end_x_count < end_y_count:
	end_y = y + end_x_count
      else:
	end_x = x + end_y_count
    return start_x, start_y, end_y, end_y

  def serial(self, checkers):
    num = 0
    last = -1
    for checker in checkers:
      if checker == -1:
	continue
      if num == 0:
	last = checker
	num += 1
	continue
      if last == checker:
	num += 1
      else:
	num = 0
      if num == 5:
	return True
    return False

  def around(self, x, y):
    a = []
    if x != 0:
      if y != 0: a.append([x-1, y-1])
      a.append([x-1, y])
      if y != 8: a.append([x-1, y+1])
    if y != 0: a.append([x, y-1])
    if y != 8: a.append([x, y+1])
    if x != 8:
      if y != 0: a.append([x+1, y-1])
      a.append([x+1, y])
      if y != 8: a.append([x+1, y+1])
    debug('a: ' + str(a))
    if not a:
      for i in range(9):
	for j in range(9):
	  if self.steps[i][j] != -1:
	    a.append([i, j])
    return a

class Node:
  def __init__(self, x, y, w, v):
    self.x = x
    self.y = y
    self.w = w
    self.v = v
    self.parent = None
    self.children = []

  def add(self, child):
    child.parent = self
    self.children.append(child)

  def is_leaf(self):
    if not self.children:
      return True
    return False

  def __str__(self):
    s = str(self.x) + ',' + str(self.y) + ':' + str(self.w) + '/' + str(self.v)
    if self.children:
      s += ' -> '
    else:
      s += ' . '
    for child in self.children:
      s += str(child)
    return s

def selection_value(node, total):
  return float(node.w) / node.v + math.sqrt(2 * math.log(total) / node.v)

def selection(node):
  total = node.v
  return sorted(node.children, key = lambda child: selection_value(child, total))[-1]

def go():
  root = Node(4, 4, 0, 1)
  chess = 1
  book = 1
  for i in range(train_num):
    board = Board()
    board.add(4, 4, chess)
    is_terminal = False
    node = root

    # Selection
    if node.children:
      debug('>>selection')
      node = selection(node)
      chess = 2
      board.add(node.x, node.y, chess)
      while True:
	if node.children and not is_terminal:
	  chess = 3 - chess
	  node = selection(node)
	  board.add(node.x, node.y, chess)
	  is_terminal = board.terminal()
	else:
	  break

    if is_terminal:
      info('chess book ' + str(book) + '\n' + str(root))
      root = Node(4, 4, 0, 1)
      book += 1
      continue

    # Expansion
    debug('>>expansion')
    next_nodes = board.around(node.x, node.y)
    next_node = random.choice(next_nodes)
    debug('next_node:' + str(next_node))
    add_node = Node(next_node[0], next_node[1], 0, 0)
    node.add(add_node)
    node = add_node
    chess = 3 - chess
    board.add(next_node[0], next_node[1], chess)
    debug(str(board.steps));

    # Simulation
    debug('>>Simulation')
    while True:
      if board.terminal():
	break
      next_steps = board.around(board.x, board.y)
      next_step = random.choice(next_steps)
      debug('next_step:' + str(next_step))
      chess = 3 - chess
      board.add(next_step[0], next_step[1], chess)
    win = 0
    if chess == 1:
      win = 1
    node.w = win
    node.v = 1

    # Backpropagation
    debug('>>Backpropagation')
    debug('node parent' + str(node.parent))
    while node.parent:
      node.parent.v += 1
      node.parent.w += win
      node = node.parent
    debug('node' + str(node))

if __name__ == '__main__':
  log('go5')
  go()
