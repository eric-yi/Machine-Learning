#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

_text_example = 'In the fields of computational linguistics and probability, an n-gram is a contiguous sequence of n items from a given sequence of text or speech. The items can be phonemes, syllables, letters, words or base pairs according to the application. The n-grams typically are collected from a text or speech corpus. When the items are words, n-grams may also be called shingles.'
_n = 1

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

def head(suffix):
    debug('===============' + suffix + ' start===============')

def tail(suffix):
    debug('===============' + suffix + ' end===============')

def open_stopWord():
    f = open('../resources/english_stopWord.txt', 'r')
    stop_words =  f.readlines()
    return map(lambda x: x.strip().lower(), stop_words)

def invoke_idf(base, tf):
    head('invoke_idf')
    file_list = filter(lambda f: f.endswith('.doc'), os.listdir(base))
    path_list = map(lambda f: base+'/'+f, file_list)
    #debug('path_list: ' + str(path_list))
    docs = []
    for path in path_list:
        rs = open(path, 'r')
        docs.append(map(lambda x: x.strip().lower(), rs.readlines()))

    _idf = {}
    for key in tf.keys():
        _idf[key] = 0
        for doc in docs:
            if key in doc[0].lower():
                _idf[key] = 1
                break

    debug('invoke idf _idf:' + str(_idf))

    tail('invoke_idf')
    return _idf

def invoke_wash(strs, stop_words):
    head('invoke_wash')
    _splits = strs.split()
    debug(_splits)
    wash_list = []
    size = len(_splits)
    #delete stop word
    splits = []
    for _split in _splits:
        if _split.lower() not in stop_words:
            splits.append(_split)

    _size = len(splits)
    debug('stop_words: ' + str(stop_words))
    m = 0
    while m < _size:
        _next = m + _n
        entry = splits[m : _next]
        wash_list.append(entry)
        m += 1

    tail('invoke_wash')
    return wash_list

def invoke_tf(wash_list):
    head('invoke_tf')
    tf = {}
    for wash in wash_list:
        wash_str = wash[0]
        if not tf.has_key(wash_str):
            tf_size = len(filter(lambda w: w[0]==wash_str, wash_list))
            #debug('wash size ' + wash_str + ':' + str(tf_size))
            tf[wash_str] = tf_size

    wash_size = len(wash_list)
    for key in tf:
        tf[key] = float(tf[key]) / wash_size

    debug('tf: ' + str(tf))

    tail('invoke_tf')
    return tf

def invoke_tfidf(tf, idf):
    head('invoke_tfidf')
    _tfidf = {}
    for key in tf.keys():
        _tfidf[key] = tf[key] * idf[key]

    tail('invoke_tfidf')
    return _tfidf

def invoke_tf_in_dir(dir, stop_words):
    pass


def main():
    stop_words = open_stopWord()
    wash_list = invoke_wash(_text_example, stop_words)
    tf = invoke_tf(wash_list)
    idf = invoke_idf('../resources', tf)
    tfidf = invoke_tfidf(tf, idf)
    debug('tfidf: ' + str(tfidf))


if __name__ == '__main__':
    print 'n-gram'
    main()

