#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import sys
sys.path.append('../src')
import app

class TestCase(unittest.TestCase):
    @unittest.skip('skip')
    def test_run(self):
        app.run()
        self.assertTrue(True)

    @unittest.skip('skip')
    def test_load_csv(self):
        csv_file = '../logs/train_categorical.csv'
        app.load_csv(csv_file, -1)
        self.assertTrue(True)

    @unittest.skip('skip')
    def test_load_labels(self):
        data_lables = app.load_labels()
        print data_lables
        self.assertTrue(len(data_lables) > 0)

    def test_truncate(self):
        factor = 100
        csv_files = ['../logs/train_categorical.csv',
                     '../logs/train_date.csv',
                     '../logs/train_numeric.csv']
        dst_files = ['../logs/train_categorical_%d.csv' % (factor),
                     '../logs/train_date_%d.csv' % (factor),
                     '../logs/train_numeric_%d.csv' % (factor)]
        app.truncate(csv_files, dst_files, factor)
        self.assertTrue(True)

unittest.main()
