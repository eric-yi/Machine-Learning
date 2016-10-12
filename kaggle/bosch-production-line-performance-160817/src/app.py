#!/usr/bin/env python
# -*- coding:utf-8 -*-

import csv
import random
from numpy import *
from types import *
import matplotlib
import matplotlib.pyplot as plt

ROOT = '../logs'
TRAIN_CATEGORICAL = 'train_categorical'
TRAIN_DATE = 'train_date'
TRAIN_NUMERIC = 'train_numeric'
FEATURES = 'features'
SUFFIX = 'csv'

TRAIN_CATEGORICAL_FILE = '%s/%s.%s' % (ROOT, TRAIN_CATEGORICAL, SUFFIX)
TRAIN_DATE_FILE = '%s/%s.%s' % (ROOT, TRAIN_DATE, SUFFIX)
TRAIN_NUMERIC_FILE = '%s/%s.%s' % (ROOT, TRAIN_NUMERIC, SUFFIX)
TRAIN_NUMERIC_FAILED_FILE = '%s/%s_failed.%s' % (ROOT, TRAIN_NUMERIC, SUFFIX)
CATEGORICAL_FEATURES_FILE = '%s/categorical_%s.%s' % (ROOT, FEATURES, SUFFIX)
DATE_FEATURES_FILE = '%s/date_%s.%s' % (ROOT, FEATURES, SUFFIX)
NUMERIC_FEATURES_FILE = '%s/numeric_%s.%s' % (ROOT, FEATURES, SUFFIX)

ARRANGE_FILE = '%s/arrange_%d.%s' % (ROOT, 100, SUFFIX)


def load_analysis_train_files(factor=100):
    return [CATEGORICAL_FEATURES_FILE, DATE_FEATURES_FILE, NUMERIC_FEATURES_FILE,
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

def save_feature(csv_file, features_file):
    features = load_features(csv_file)
    _file = open(features_file, 'w')
    _file.write(features)

def save_features():
    save_feature(TRAIN_CATEGORICAL_FILE, CATEGORICAL_FEATURES_FILE)
    save_feature(TRAIN_DATE_FILE, DATE_FEATURES_FILE)
    save_feature(TRAIN_NUMERIC_FILE, NUMERIC_FEATURES_FILE)

def save_failed_numeric(csv_file=TRAIN_NUMERIC_FILE, failed_file=TRAIN_NUMERIC_FAILED_FILE):
    datalist = load_csv(csv_file)
    _file = open(failed_file, 'w')
    _file.write(datalist[0])
    _file.write('\n')
    m = 1
    while m < len(datalist):
        data = datalist[m]
        if int(data.split(',')[-1]) == 1:
            _file.write(data)
            _file.write('\n')
        m += 1

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

def save_arrange(arrange_file=ARRANGE_FILE):
    analysis_train_files = load_analysis_train_files()

    categorical_features_file = analysis_train_files[0]
    categorical_features = load_features(categorical_features_file).split(',')
    #print categorical_features
    date_features_file = analysis_train_files[1]
    date_features = load_features(date_features_file).split(',')
    #print date_features
    numeric_features_file = analysis_train_files[2]
    numeric_features = load_features(numeric_features_file).split(',')
    #print numeric_features

    feature_mapping = {}
    categorical_feature_mapping = {}
    numeric_feature_mapping = {}
    m = 1
    categorical_feature_size = len(categorical_features)
    #print categorical_feature_size
    while m < categorical_feature_size:
        feature_mapping[categorical_features[m]] = 0
        categorical_feature_mapping[categorical_features[m]] = m
        m += 1
    m = 1
    numeric_feature_size = len(numeric_features)
    #print numeric_feature_size
    while m < (numeric_feature_size - 1):
        feature_mapping[numeric_features[m]] = 0
        numeric_feature_mapping[numeric_features[m]] = m
        m += 1
    feature_list = []
    for feature in feature_mapping:
        feature_list.append(feature)
    feature_list = sorted(feature_list)
    #print feature_list
    #print len(feature_list)

    feature_size = len(feature_list)
    date_feature_size = len(date_features)
    #print date_feature_size
    feature_merger = []
    m = 0
    while m < feature_size:
        feature_entry = {}
        name = feature_list[m]
        feature_entry['name'] = name
        if categorical_feature_mapping.has_key(name):
            feature_entry['categorical_column'] = categorical_feature_mapping[name]
        if numeric_feature_mapping.has_key(name):
            feature_entry['numeric_column'] = numeric_feature_mapping[name]
        feature_entry['column'] = m
        names = name.split('_')
        date_expect = '%s_%s_D%d' % (names[0], names[1], int(names[2][1:])+1)
        j = 1
        while j < date_feature_size:
            if date_features[j] == date_expect:
                feature_entry['date_name'] = date_expect
                feature_entry['date_column'] = j
                #print name
                #print date_expect
                break
            j += 1
        feature_merger.append(feature_entry)
        m += 1

    train_categorical_file = analysis_train_files[3]
    train_categorical = load_csv(train_categorical_file)
    train_date_file = analysis_train_files[4]
    train_date = load_csv(train_date_file)
    train_numeric_file = analysis_train_files[5]
    train_numeric = load_csv(train_numeric_file)

    n = 0
    line = len(train_categorical)
    analysis_list = []
    _file = open(arrange_file, 'w')
    while n < line:
        categorical = train_categorical[n].split(',')
        #print len(categorical)
        date = train_date[n].split(',')
        numeric = train_numeric[n].split(',')
        #print len(numeric)
        analysis = []
        analysis.append(categorical[0])
        buf = '%s' % (categorical[0])
        m = 0
        while m < feature_size:
            analysis_rows = []
            feature_dict = feature_merger[m]
            name = feature_dict['name']
            analysis_rows.append(name)
            _categorical = 0
            if categorical_feature_mapping.has_key(name):
                _categorical = format_value(categorical[categorical_feature_mapping[name]])
            analysis_rows.append(_categorical)
            _numeric = 0
            if numeric_feature_mapping.has_key(name):
                _numeric = format_value(numeric[numeric_feature_mapping[name]])
            analysis_rows.append(_numeric)
            if feature_dict.has_key('date_name'):
                analysis_rows.append(format_value(feature_dict['date_name']))
                analysis_rows.append(format_value(date[int(feature_dict['date_column'])]))
            else:
                analysis_rows.append(0)
                analysis_rows.append(0)
            #print analysis_rows
            value = '%s->%s->%s->%s->%s' % (
                analysis_rows[0],
                analysis_rows[3],
                analysis_rows[1],
                analysis_rows[2],
                analysis_rows[4])
            #print value
            buf = '%s, %s' % (buf, value)
            analysis.append(value)
            m += 1
        #print numeric[-1]
        analysis.append(numeric[-1])
        buf = '%s, %s\n' % (buf, numeric[-1])
        _file.write(buf)
        #print analysis
        analysis_list.append(analysis)
        n += 1

def format_value(value):
    if value and len(value) > 0:
        return value
    return 0

def load_categorical_sample_data():
    analysis_train_files = load_analysis_train_files()
    train_categorical_file = analysis_train_files[3]
    train_categorical_data = load_csv(train_categorical_file)
    return [map(lambda x: 0 if x == '' else float(x[1:]), line.split(',')) for line in train_categorical_data]

def load_date_sample_data():
    analysis_train_files = load_analysis_train_files()
    train_date_file = analysis_train_files[4]
    train_date_data = load_csv(train_date_file)
    return [map(lambda x: 0 if x == '' else float(x), line.split(',')) for line in train_date_data]

def load_numeric_sample_data():
    analysis_train_files = load_analysis_train_files()
    train_numeric_file = analysis_train_files[5]
    train_numeric_data = load_csv(train_numeric_file)
    return [map(lambda x: 0 if x == '' else float(x), line.split(',')) for line in train_numeric_data]


def sigmoid(x):
    return 1.0 / (1 + exp(-x))

def init_categorical_and_date_data(data):
    # init
    mat_data = mat(data)
    m, n = shape(mat_data)
    ids = mat_data[:, 0]
    datas = mat_data[:, 1:]

    return ids, datas

def init_numeric_data(data):
    # init
    mat_data = mat(data)
    m, n = shape(mat_data)
    results = mat_data[:, n-1]
    ids = mat_data[:, 0]
    datas = mat_data[:, 1:n-1]

    return ids, datas, results

def with_logistic(data=load_numeric_sample_data(), loop=500):
    # init
    ids, datas, results = init_numeric_data(data)

    # compute
    m, n = shape(datas)
    weights = ones((n, 1))
    for j in range(loop):
        data_index = range(m)
        for i in range(m):
            alpha = 4 / (1.0 + j + i) + 0.001
            rand_index = int(random.uniform(0, len(data_index)))
            h = sigmoid(sum(datas[rand_index] * weights))
            error = results[i] - h
            #print error
            weights = weights + (alpha * error * datas[rand_index]).transpose()
            del(data_index[rand_index])
    classify(datas, results, weights)
    return weights

def classify(datas, results, weights):
    n = 0
    for data in datas:
        total = sum(data * weights)
        probe = sigmoid(total)
        #print probe
        result = results[n]
        if int(result) == 1:
            print probe
            print '%f, %f\n' % (total, result)
        n += 1

def calcute_feature_count(datas):
    m, n = shape(datas)
    j = 0
    counts = []
    while j < n:
        data = datas[:, j]
        data_m, data_n = shape(data[data > 0])
        counts.append(data_n)
        j += 1
    return counts

def get_result_list():
    analysis_train_files = load_analysis_train_files()
    train_numeric_file = analysis_train_files[5]
    train_numeric_data = load_csv(train_numeric_file)
    return [float(line.split(',')[-1]) for line in train_numeric_data]

def calcute_failed_feature_count(results_statistics, datas):
    failed_list = []
    i = 0
    for statistics in results_statistics:
        if (type(statistics) is ListType and statistics[-1] == 1.0) \
           or (type(statistics) is FloatType and statistics == 1.0):
            failed_list.append(datas[i, :].tolist()[0])
        i += 1

    return calcute_feature_count(mat(failed_list))

def merge_feature_counts(full_counts, failed_counts):
    counts = []
    n = len(full_counts)
    i = 0
    while i < n:
        counts.append([full_counts[i], failed_counts[i]])
        i += 1
    return counts

def analysis_numeric(data=load_numeric_sample_data()):
    # init
    ids, datas, results = init_numeric_data(data)
    print shape(datas)
    mean_datas = mean(datas, axis = 0)
    #print mean_datas
    full_counts = calcute_feature_count(datas)
    #print full_counts
    #print len(full_counts)

    m, n = shape(datas)
    i = 0
    results_statistics = []
    result_list = results.tolist()
    id_list = ids.tolist()
    while i < m:
        data = datas[i, :]
        data_m, data_n = shape(data[data > 0])
        result = result_list[i][0]
        id = id_list[i][0]
        results_statistics.append([id, data_n, sum(data), result]);
        i += 1
    #print results_statistics

    failed_counts = calcute_failed_feature_count(results_statistics, datas)
    #print failed_counts
    #print len(failed_counts)

    counts = merge_feature_counts(full_counts, failed_counts)
    print counts
    print sorted(counts, reverse=True)

    #draw_feature_counts(sorted(full_counts))
    draw_feature_counts(sorted(failed_counts))

def draw_feature_counts(counts, x=1):
    #fig = plt.figure()
    plt.plot(counts)
    plt.show()

def analysis_categorical(data=load_categorical_sample_data()):
    # init
    ids, datas = init_categorical_and_date_data(data)
    full_counts = calcute_feature_count(datas)
    #print full_counts
    result_list = get_result_list()
    #print len(result_list)
    failed_counts = calcute_failed_feature_count(result_list, datas)
    #print failed_counts

    print len(full_counts)
    print len(failed_counts)
    counts = merge_feature_counts(full_counts, failed_counts)
    print counts
    print sorted(counts, reverse=True)
    #draw_feature_counts(sorted(full_counts))
    draw_feature_counts(sorted(failed_counts))

def analysis_date(data=load_date_sample_data()):
    # init
    ids, datas = init_categorical_and_date_data(data)
    full_counts = calcute_feature_count(datas)
    #print full_counts
    result_list = get_result_list()
    #print len(result_list)
    failed_counts = calcute_failed_feature_count(result_list, datas)
    #print failed_counts

    print len(full_counts)
    print len(failed_counts)
    counts = merge_feature_counts(full_counts, failed_counts)
    print counts
    print sorted(counts, reverse=True)
    #draw_feature_counts(sorted(full_counts))
    draw_feature_counts(sorted(failed_counts))


def with_pca(data=load_numeric_sample_data()):
    pass

def run():
    print 'start run...'
