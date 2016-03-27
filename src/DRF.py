#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Dominant Resource Fairness
--------------------------
Refererence Paper: EECS-2010-55.pdf
Link: <a href='http://www.eecs.berkeley.edu/Pubs/TechRpts/2010/EECS-2010-55.pdf'>EECS-2010-55.pdf</a>
---
12/26/2015 xbyi@thoughtworks.com
"""

_debug = True
_debug = False

"""
test datas
----------
"""
resource_name = ('cpu', 'memory')
resources = ((2, 1), (5, 2), (3, 2))
weights = ((2, 1), (1, 2), (1, 2))
#weights = ()
total = (500, 240)

"""
tool functions
--------------
"""
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

def rate(elements, sums):
  return list(map(lambda element:list(map(lambda (i,e):float(e)/sums[i], enumerate(element))), elements))

def sum_2(arr, size):
  _sum = [0] * size
  for a in arr:
    for i, b in enumerate(a):
      _sum[i] += b
  return _sum

def max(arr):
  _diff = lambda a, b : a if (a > b) else b
  return reduce(_diff, arr)

def add(l1, l2):
  return map(lambda x,y: x+y, l1,l2)

def add_2(l1, l2):
  return map(lambda x,y: add(x,y), l1,l2)

def divide(l1, l2):
  return map(lambda x,y: x*y, l1,l2)

"""
main function
-------------
"""
# global datas
res_shares = []
dom_shares = []
total_alloc = []
_shares = []
_weights = []

def show():
  _total_show = map(lambda x,y: '%s->%s' % (str(x),str(y)), resource_name,total)
  info(_total_show)
  if len(weights) > 0:
    _resource_show = map(lambda resource,weight: map(lambda x,y,z: '%s->%s->%s' % (str(x),str(y),str(z)), resource_name,resource,weight), resources,weights)
  else:
    _resource_show = map(lambda resource: map(lambda x,y: '%s->%s' % (str(x),str(y)), resource_name,resource), resources)
  info(_resource_show)

def init():
  global res_shares, dom_shares, total_alloc, _shares, _weights
  res_shares = [[0] * len(resource_name)] * len(resources)
  dom_shares = [0] * len(resources)
  total_alloc = [0] * len(total)
  _shares = rate(resources, total)
  if len(weights) > 0:
    _weights = rate(weights, sum_2(weights, len(total)))
  else:
    _weights = [[1] * len(resource_name)] * len(resources)

def compute():
  global res_shares, dom_shares, total_alloc, _shares, _weights
  temp_shares = _shares

  count = 0
  while True:
    count += 1
    max_alloc = -1
    index_alloc = 0
    for i, s in enumerate(temp_shares):
      temp_max = max(divide(s, _weights[i]))
      if max_alloc == -1 or temp_max < max_alloc:
        max_alloc = temp_max
        index_alloc = i

    share_alloc = _shares[index_alloc]
    total_alloc = add(total_alloc, share_alloc)
    if False in map(lambda x: x<=1, total_alloc):
      break
    res_shares[index_alloc] = add(res_shares[index_alloc], share_alloc)
    dom_shares[index_alloc] = max(res_shares[index_alloc])
    temp_shares = add_2(res_shares, _shares)
    info('-----------------------')
    info('count', count)
    info('alloc resource',  index_alloc, resources[index_alloc])
    info('resource shares', res_shares)
    info('dominate shares', dom_shares)
    info('total alloc', total_alloc)

def DRF():
  log('step 1', 'show input datas')
  show()
  log('step 2', 'initalize')
  init()
  log('step 3', 'compute')
  compute()

if __name__ == '__main__':
  log('DRF - Dominant Resource Fairness')
  DRF()
