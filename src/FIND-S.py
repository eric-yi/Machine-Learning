#!/usr/bin/python
# -*- coding: utf-8 -*-
from COMMON import *

def FIND_S(e, length):
  #print(e)
  s = []
  n = 0
  while n < length:
    s.append(SPECIAL)
    n += 1;
  for entry in e:
    if entry.keys()[0] == "Yes":
      value = entry["Yes"]
      n = 0
      while n < length:
        v = value[n]
        ss = s[n]
        if ss == SPECIAL:
          ss = v
        elif ss != v:
          ss = GENERAL
        s[n] = ss
        n += 1;

  return s

if __name__ == "__main__":
  print("FIND-S")
  S = FIND_S(Sport, 6)
  print(S)
