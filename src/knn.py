#!/usr/bin/python
# -*- coding: utf-8 -*-

from numpy import *
import operator

def createDataSet():
    group = array([ [1.0, 1.1] , [1.0, 1.0], [0, 0], [0, 0.1] ])
    lables = ['A', 'A', 'B', 'B']
    return group, lables

group, labels = createDataSet()

example = [
    [3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2], [18, 90]
]

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[O]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum (axis=l)
    distances = sqDistances ** 0.5
    sortedDistIndicies - distances.argaort()
    classCount = { }
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[votellabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(l), reverse=True)
    return sortedClassCount[0][0]

classify0(2, example, labels, 10)
