#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import sys
sys.path.append('../src')
import app
from numpy import *

class TestCase(unittest.TestCase):
    @unittest.skip('skip')
    def test_run(self):
        app.run()
        self.assertTrue(True)

    @unittest.skip('skip')
    def test_load_analysis_train_files(self):
        analysis_train_files = app.load_analysis_train_files()
        self.assertEqual(len(analysis_train_files), 6)
        self.assertEqual(analysis_train_files[0], app.CATEGORICAL_FEATURES_FILE)
        self.assertEqual(analysis_train_files[3], '../logs/train_categrical_100.csv')
        self.assertEqual(analysis_train_files[4], '../logs/train_date_100.csv')
        self.assertEqual(analysis_train_files[5], '../logs/train_numeric_100.csv')

    @unittest.skip('skip')
    def test_load_csv(self):
        csv_file = '../logs/train_categorical.csv'
        app.load_csv(csv_file, -1)
        self.assertTrue(True)

    @unittest.skip('skip')
    def test_load_features(self):
        features = app.load_features()
        print features
        self.assertTrue(len(features) > 0)

    @unittest.skip('skip')
    def test_save_features(self):
        app.save_features()
        self.assertTrue(True)

    @unittest.skip('skip')
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

    @unittest.skip('skip')
    def test_save_arrange(self):
        app.save_arrange()
        self.assertTrue(True)

    @unittest.skip('skip')
    def test_save_failed_numeric(self):
        app.save_failed_numeric()
        self.assertTrue(True)

    @unittest.skip('skip')
    def test_with_logistic(self):
        app.with_logistic()
        self.assertTrue(True)

    @unittest.skip('skip')
    def test_load_categorical_sample_data(self):
        categorical = app.load_categorical_sample_data()
        print shape(categorical)
        self.assertTrue(True)

    @unittest.skip('skip')
    def test_load_date_sample_data(self):
        date = app.load_date_sample_data()
        print shape(date)
        self.assertTrue(True)

    @unittest.skip('skip')
    def test_load_numeric_sample_data(self):
        numeric = app.load_numeric_sample_data()
        print shape(numeric)
        self.assertTrue(True)

    @unittest.skip('skip')
    def test_analysis_numeric(self):
        app.analysis_numeric()
        self.assertTrue(True)

    @unittest.skip('skip')
    def test_analysis_categorical(self):
        app.analysis_categorical()
        self.assertTrue(True)

    @unittest.skip('skip')
    def test_analysis_date(self):
        app.analysis_date()
        self.assertTrue(True)

    @unittest.skip('skip')
    def test_with_pca(self):
        app.with_pca()
        self.assertTrue(True)

    #@unittest.skip('skip')
    def test_decrease_dim(self):
        app.decrease_dim()
        self.assertTrue(True)

unittest.main()
