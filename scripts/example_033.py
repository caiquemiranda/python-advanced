# -*- coding: utf-8 -*-
"""
@filename: example_033.py
@author: Caique Miranda
"""
# Example - 033


class DurgaMath:

    @staticmethod
    def add(x, y):
        print('The Sum:', x+y)

    @staticmethod
    def product(x, y):
        print('The Product:', x*y)

    @staticmethod
    def average(x, y):
        print('The average:', (x+y)/2)


DurgaMath.add(10, 20)
DurgaMath.product(10, 20)
DurgaMath.average(10, 20)
