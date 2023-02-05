# -*- coding: utf-8 -*-
"""
@filename: example_035.py
@author: Caique Miranda
"""
# Example - 035


class Outer:

    def __init__(self):

        print("outer class object creation")


class Inner:

    def __init__(self):

        print("inner class object creation")

    def m1(self):

        print("inner class method")


o = Outer()
i = o.Inner()
i.m1()
