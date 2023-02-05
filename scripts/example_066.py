# -*- coding: utf-8 -*-
"""
@filename: example_066.py
@author: Caique Miranda
"""
# Example - 066


class P:

    a = 10

    def __init__(self):
        self.b = 10

    def m1(self):
        print('Parent instance method')

    @classmethod
    def m2(cls):
        print('Parent class method')

    @staticmethod
    def m3():
        print('Parent static method')


class C(P):

    a = 888

    def __init__(self):
        self.b = 999
        super().__init__()
        print(super().a)
        super().m1()
        super().m2()
        super().m3()


c = C()
