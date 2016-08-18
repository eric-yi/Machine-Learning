#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __init__ import *
from nGram import *

class TestCase(unittest.TestCase):
    def test_sayHello(self):
        self.assertTrue(True)

    def test_invoke_tf_in_dir(self):
        dir = 'resources'
        stop_words = open_stopWord()
        self.assertTrue(len(stop_words) > 0)
        invoke_tf_in_dir(dir, stop_words)
        self.assertTrue(True)

unittest.main()
