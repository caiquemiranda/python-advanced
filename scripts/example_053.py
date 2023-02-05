# -*- coding: utf-8 -*-
"""
@filename: example_053.py
@author: Caique Miranda
"""
# Example - 053


class P:

    def __init__(self):
        print(id(self))


class C(P):
    pass


c = C()
print(id(c))
