#!/usr/bin/env python
# -*- coding:utf-8 -*-

import csv

def load_csv(csv_file, rows):
    datalist = []
    with open(csv_file, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        n = 0
        for row in reader:
            if n >= rows: break
            datalist.append(row[0])
            n += 1
    return datalist


TRAIN_CATEGORICAL = '../logs/train_categorical.csv'
def load_labels(csv_file=TRAIN_CATEGORICAL):
    return load_csv(csv_file, 1)[0]

def run():
    print 'start run...'
