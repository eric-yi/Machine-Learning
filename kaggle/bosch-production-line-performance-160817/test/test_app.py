#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import sys
sys.path.append('../src')
import app

class TestCase(unittest.TestCase):
    def test_run(self):
        app.run()
        self.assertTrue(True)

    def test_load_csv(self):
        csv_file = '../logs/train_categorical.csv'
        app.load_csv(csv_file, 10)
        self.assertTrue(True)

unittest.main()