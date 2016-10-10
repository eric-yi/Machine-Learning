#!/usr/bin/env python
# -*- coding:utf-8 -*-

import csv
import random

ROOT = '../logs'
TRAIN_CATEGORICAL = 'train_categorical'
TRAIN_DATE = 'train_date'
TRAIN_NUMERIC = 'train_numeric'
FEATURES = 'features'
SUFFIX = 'csv'

TRAIN_CATEGORICAL_FILE = '%s/%s.%s' % (ROOT, TRAIN_CATEGORICAL, SUFFIX)
TRAIN_DATE_FILE = '%s/%s.%s' % (ROOT, TRAIN_DATE, SUFFIX)
TRAIN_NUMERIC_FILE = '%s/%s.%s' % (ROOT, TRAIN_NUMERIC, SUFFIX)
FEATURES_FILE = '%s/%s.%s' % (ROOT, FEATURES, SUFFIX)

def load_analysis_train_files(factor=100):
    return [FEATURES_FILE,
            ('%s/%s_%d.%s' % (ROOT, TRAIN_CATEGORICAL, factor, SUFFIX)),
            ('%s/%s_%d.%s' % (ROOT, TRAIN_DATE, factor, SUFFIX)),
            ('%s/%s_%d.%s' % (ROOT, TRAIN_NUMERIC, factor, SUFFIX))]


def load_csv(csv_file, rows=-1):
    datalist = []
    with open(csv_file, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        n = 0
        for row in reader:
            if rows != -1 and n >= rows: break
            datalist.append(row[0])
            n += 1
    return datalist


def load_features(csv_file=TRAIN_CATEGORICAL_FILE):
    return load_csv(csv_file, 1)[0]

def save_features(csv_file=TRAIN_CATEGORICAL_FILE, features_file=FEATURES_FILE):
    features = load_features()
    _file = open(features_file, 'w')
    _file.write(features)

def truncate(csv_files, dst_files, factor=100):
    datalist_group = []
    for csv_file in csv_files:
        datalist = load_csv(csv_file)
        datalist_group.append(datalist)
    truncate_file_group = []
    for dst_file in dst_files:
        truncate_file = open(dst_file, 'w')
        truncate_file_group.append(truncate_file)
    n = 0
    size = len(datalist)
    while True:
        start = n * factor
        index = start + int(random.random() * factor)
        if index > size:    break
        m = 0
        while m < len(datalist_group):
            datalist = datalist_group[m]
            truncate_file = truncate_file_group[m]
            truncate_file.write(datalist[index])
            truncate_file.write('\n')
            m += 1
        n += 1

def analysis():
    analysis_train_files = load_analysis_train_files()
    features_file = analysis_train_files[0]
    train_categorical_file = analysis_train_files[1]
    train_date_file = analysis_train_files[2]
    train_numeric_file = analysis_train_files[3]


def run():
    print 'start run...'
