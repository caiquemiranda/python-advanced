# -*- coding: utf-8 -*-
"""
@filename: example_013.py
@author: Caique Miranda
"""
# Example - 013


class Test:

    def __init__(self):
        self.a = 10
        self.b = 20


t1 = Test()
t1.a = 888

t1.b = 999
t2 = Test()

print('t1:', t1.a, t1.b)
print('t2:', t2.a, t2.b)
