# -*- coding: utf-8 -*-
"""
@filename: example_055.py
@author: Caique Miranda
"""
# Example - 55


class P:

    def m1(self):
        print("Parent Method")


class C(P):

    def m2(self):
        print("Child Method")


c = C()
c.m1()
c.m2()
