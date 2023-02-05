# -*- coding: utf-8 -*-
"""
@filename: example_056.py
@author: Caique Miranda
"""
# Example - 056


class P:

    def m1(self):
        print("Parent Method")


class C(P):

    def m2(self):
        print("Child Method")


class CC(C):

    def m3(self):
        print("Sub Child Method")


c = CC()
c.m1()
c.m2()
c.m3()
