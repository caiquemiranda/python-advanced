# -*- coding: utf-8 -*-
"""
@filename: example_072.py
@author: Caique Miranda
"""
# Example - 072


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

    @staticmethod
    def m1():
        super().m1()  # -->invalid
        super().m2()  # --->invalid
        super().m3()  # --->invalid


C.m1()
