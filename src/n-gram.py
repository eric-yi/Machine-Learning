#!/usr/bin/env python
# -*- coding:utf-8 -*-

_text_exmaple = 'In the fields of computational linguistics and probability, an n-gram is a contiguous sequence of n items from a given sequence of text or speech. The items can be phonemes, syllables, letters, words or base pairs according to the application. The n-grams typically are collected from a text or speech corpus. When the items are words, n-grams may also be called shingles.'
_n = 2

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


def nGram():
    _splits = _text_exmaple.split()
    debug(_splits)
    gram_list = []
    size = len(_splits)
    m = 0
    while m < size:
        _next = m + _n
        entry = _splits[m : _next]
        gram_list.append(entry)
        m += 1
    info('gram list:' + str(gram_list))


if __name__ == '__main__':
    print 'n-gram'
    nGram()
