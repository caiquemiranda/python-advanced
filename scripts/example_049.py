# -*- coding: utf-8 -*-
"""
@filename: example_049.py
@author: Caique Miranda
"""
# Example - 049


class P:

    a = 10

    def __init__(self):
        self.b = 20


class C(P):

    c = 30

    def __init__(self):
        super().__init__()  # ===>Line-1
        self.d = 30


c1 = C()
print(c1.a, c1.b, c1.c, c1.d)
