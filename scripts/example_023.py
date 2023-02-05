# -*- coding: utf-8 -*-
"""
@filename: example_023.py
@author: Caique Miranda
"""
# Example - 023


class Test:

    a = 10

    @classmethod
    def m1(cls):
        del cls.a


Test.m1()
print(Test.__dict__)
