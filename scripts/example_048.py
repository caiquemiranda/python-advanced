# -*- coding: utf-8 -*-
"""
@filename: example_048.py
@author: Caique Miranda
"""
# Example - 048


class P:

    def m1(self):
        print("Parent class method")


class C(P):

    def m2(self):
        print("Child class method")


c = C()
c.m1()
c.m2()
