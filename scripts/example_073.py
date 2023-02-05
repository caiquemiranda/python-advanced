# -*- coding: utf-8 -*-
"""
@filename: example_073.py
@author: Caique Miranda
"""
# Example - 073


class A:

    @staticmethod
    def m1():
        print('Parent static method')


class B(A):

    @staticmethod
    def m2():
        super(B, B).m1()


B.m2()
