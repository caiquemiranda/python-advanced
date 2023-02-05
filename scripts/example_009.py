# -*- coding: utf-8 -*-
"""
@filename: example_009.py
@author: Caique Miranda
"""
# Example - 009


class Test:

    def __init__(self):

        self.a = 10
        self.b = 20

    def m1(self):

        self.c = 30


t = Test()
t.m1()
t.d = 40
print(t.__dict__)
