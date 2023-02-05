# -*- coding: utf-8 -*-
"""
@filename: example_069.py
@author: Caique Miranda
"""
# Example - 069


class P:

    def __init__(self):
        print('Parent Constructor')

    def m1(self):
        print('Parent instance method')

    @classmethod
    def m2(cls):
        print('Parent class method')

    @staticmethod
    def m3():
        print('Parent static method')


class C(P):

    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

    def m1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()


c = C()
c.m1()
