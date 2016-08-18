#!/usr/bin/env python
# -*- coding:utf-8 -*-

from google_ngram_downloader import readline_google_store
fname, url, records = next(readline_google_store(ngram_len=5))

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

test_path = 'test_data/SystemOut.log'
sw_list = []

def load_stop_words():
    resource_list = ['resources/chinese_stopWord.txt', 'resources/english_stopWord.txt',
                'resources/sign_stopWord.txt', 'resources/union_stopWord.txt']
    # resource_list = ['resources/english_stopWord.txt']
    for res in resource_list:
        f = open(res)
        for w in f.readlines():
            sw_list.append(w.strip())
    print sw_list

def pre_handler():
    f = open(test_path)
    # remove stop words
    wash_datas = filter(lambda word:
            not filter(lambda sw: sw==word, sw_list),
            map(lambda line: line.split(), f.readlines())
            )
    debug('after remove stop word')
    debug('======================')
    debug(wash_datas)
    debug('======================')

def test_google_ngram_download():
    from google_ngram_downloader import readline_google_store
    fname, url, records = next(readline_google_store(ngram_len=5))
    debug('fname = ' + fname)
    debug('url = ' + url)

    record = next(records)
    #debug('next: ' + str(record))
    #debug('next gram: ' + str(record.ngram.encode('utf-8')))
    while record:
        ngram = record.ngram.encode('utf-8')
        if 'American' in ngram:
            debug('gram: ' + str(record))
        record = next(records)

def test_ngram():
    import ngram
    G = ngram.NGram(['chinese'])
    debug(G.search('chinese'))

def test():
    #test_ngram()
    #test_google_ngram_download()
    pass

#load_stop_words()
#pre_handler()
#test()

class TestCase(unittest.TestCase):
    def test_invoke_tf_in_dir(self):
        dir = './resources'
        n-gram.invoke_tf_in_dir(dir, stop_words)

unittest.main()
