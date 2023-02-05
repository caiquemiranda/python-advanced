# -*- coding: utf-8 -*-
"""
@filename: example_010.py
@author: Caique Miranda
"""
# Example - 010


class Test:

    def __init__(self):
        self.a = 10
        self.b = 20

    def display(self):
        print(self.a)
        print(self.b)


t = Test()
t.display()

print(t.a, t.b)
