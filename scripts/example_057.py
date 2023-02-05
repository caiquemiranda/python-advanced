# -*- coding: utf-8 -*-
"""
@filename: example_057.py
@author: Caique Miranda
"""
# Example - 057
class P:

    def m1(self):
        print("Parent Method")


class C1(P):
    def m2(self):
        print("Child1 Method")


class C2(P):
    def m3(self):
        print("Child2 Method")


c1 = C1()
c1.m1()
c1.m2()

c2 = C2()
c2.m1()
c2.m3()