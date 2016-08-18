#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __init__ import *
from utils import *

class TestCase(unittest.TestCase):
    def test_sayHello(self):
        self.assertTrue(True)

    def test_list_path(self):
        list_path('resources')
        self.assertTrue(True)

unittest.main()
