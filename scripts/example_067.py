# -*- coding: utf-8 -*-
"""
@filename: example_067.py
@author: Caique Miranda
"""
# Example - 067


class A:

    def m1(self):
        print('A class Method')


class B(A):

    def m1(self):
        print('B class Method')


class C(B):

    def m1(self):
        print('C class Method')


class D(C):

    def m1(self):
        print('D class Method')


class E(D):

    def m1(self):
        A.m1(self)


e = E()
e.m1()
