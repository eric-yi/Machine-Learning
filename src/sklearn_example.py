#!/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()
print(digits.data)
print digits.target
print digits.images[0]

from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)
print clf.fit(digits.data[:-1], digits.target[:-1])
print clf.predict(digits.data[-1:])

from sklearn import datasets
clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
print clf.fit(X, y)

import pickle
s = pickle.dumps(clf)
clf2 = pickle.loads(s)
clf2.predict(X[0:1])
print y[0]
