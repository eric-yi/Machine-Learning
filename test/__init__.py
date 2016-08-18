#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
reload(sys)
import os
import logging
import unittest

def get_src_dir():
    src_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/src"
    return src_dir

SRC_DIR = get_src_dir()

sys.path.insert(0, SRC_DIR)
