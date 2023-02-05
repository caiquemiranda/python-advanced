# -*- coding: utf-8 -*-
"""
@filename: example_068.py
@author: Caique Miranda
"""
# Example - 068


class P:

    a = 10

    def __init__(self):
        self.b = 20


class C(P):

    def m1(self):
        print(super().a)  # valid
        print(self.b)  # valid
        print(super().b)  # invalid


c = C()
c.m1()
