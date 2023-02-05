# -*- coding: utf-8 -*-
"""
@filename: example_042.py
@author: Caique Miranda
"""
# Example - 042
import sys


class Test:

    pass


t1 = Test()
t2 = t1
t3 = t1
t4 = t1

print(sys.getrefcount(t1))
