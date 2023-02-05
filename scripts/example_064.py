# -*- coding: utf-8 -*-
"""
@filename: example_064.py
@author: Caique Miranda
"""
# Example - 064


class D:
    pass


class E:
    pass


class F:
    pass


class B(D, E):
    pass


class C(D, F):
    pass


class A(B, C):
    pass


print(D.mro())
print(B.mro())
print(C.mro())
print(A.mro())
