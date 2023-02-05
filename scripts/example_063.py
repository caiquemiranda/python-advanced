# -*- coding: utf-8 -*-
"""
@filename: example_063.py
@author: Caique Miranda
"""
# Example - 063


class A:

    def m1(self):
        print('A class Method')


class B:

    def m1(self):
        print('B class Method')


class C:

    def m1(self):
        print('C class Method')


class X(A, B):

    def m1(self):
        print('X class Method')


class Y(B, C):

    def m1(self):
        print('Y class Method')


class P(X, Y, C):

    def m1(self):
        print('P class Method')


p = P()
p.m1()
