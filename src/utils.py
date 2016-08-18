#!/usr/bin/env python
# -*- coding:utf-8 -*-

def list_path(path):
    file_list = []
    _list_path(file_list, open(path))
    return list_path

def _list_path(file_list, path):
    for sub_path in path:
        if sub_path.isFile():
            path.insert(sub_path)
        else:
            list_path(file_list, sub_path)
