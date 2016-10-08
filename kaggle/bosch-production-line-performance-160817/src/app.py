#!/usr/bin/env python
# -*- coding:utf-8 -*-

import csv
import random

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


TRAIN_CATEGORICAL = '../logs/train_categorical.csv'
def load_labels(csv_file=TRAIN_CATEGORICAL):
    return load_csv(csv_file, 1)[0]

def truncate(csv_files, dst_files, factor=10):
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

def run():
    print 'start run...'
