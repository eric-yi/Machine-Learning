#!/usr/bin/env python
# -*- coding:utf-8 -*-

import math

_debug = True
#_debug = False

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


#_tree = (4, 7, (2, 3, (0, 1), (1, 2, (0, 1), (1, 1))), (1, 3, (0, 1), (1, 1), (1, 1)), (0, 1))
_tree = (11, 21, (7, 10, (2, 4), (5, 6, (2, 3), (2, 3))), (4, 8, (1, 2), (2, 3), (2, 3)), (0, 3))

class Node:
  def __init__(self, win, visit):
    self.win = win
    self.visit = visit
    self.children = []

  def add(self, child):
    self.children.append(child)

  def is_leaf(self):
    if not self.children:
      return True
    return False

  def __str__(self):
    s = str(self.win) + '/' + str(self.visit)
    if self.children:
      s += ' -> '
    else:
      s += ' . '
    for child in self.children:
      s += str(child)
    return s

def make_tree():
  tree = make_node(_tree)
  debug(tree)
  return tree

def make_node(tree):
  node = Node(tree[0], tree[1])
  for child in tree[2:]:
    child_node = make_node(child)
    node.add(child_node)
  return node

def selection_value(node, total):
  return float(node.win) / node.visit + math.sqrt(2 * math.log(total) / node.visit)

def selection(node):
  total = node.visit
  return sorted(node.children, key = lambda child: selection_value(child, total))[-1]

def MCTS():
  tree = make_tree()
  # selection
  selection_node = tree
  while not selection_node.is_leaf():
    selection_node = selection(selection_node)
    debug('W/V:' + str(selection_node.win) + '/' + str(selection_node.visit))
  # expansion



if __name__ == '__main__':
  log('MCTS - Monte Carlo Tree Search')
  MCTS()
