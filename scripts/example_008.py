# -*- coding: utf-8 -*-
"""
@filename: example_008.py
@author: Caique Miranda
"""
# Example - 008


class Test:

    def __init__(self):

        self.a = 10
        self.b = 20

        def m1(self):
            self.c = 30


t = Test()
t.m1()
print(t.__dict__)
