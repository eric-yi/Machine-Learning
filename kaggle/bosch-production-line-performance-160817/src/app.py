#!/usr/bin/env python
# -*- coding:utf-8 -*-

import csv

def load_csv(csv_file, rows):
    with open(csv_file, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        n = 0
        for row in reader:
            if n > rows: break
            print ', '.join(row)
            n += 1

def run():
    print 'start run...'
