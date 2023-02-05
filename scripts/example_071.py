# -*- coding: utf-8 -*-
"""
@filename: example_071.py
@author: Caique Miranda
"""
# Example - 071


class A:

    def __init__(self):
        print('Parent constructor')

    def m1(self):
        print('Parent instance method')


class B(A):

    @classmethod
    def m2(cls):
        super(B, cls).__init__(cls)
        super(B, cls).m1(cls)


B.m2()
