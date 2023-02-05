# -*- coding: utf-8 -*-
"""
@filename: example_062.py
@author: Caique Miranda
"""
# Example - 062
class A:
    pass


class B:
    pass


class C:
    pass


class X(A, B):
    pass


class Y(B, C):
    pass


class P(X, Y, C):
    pass


print(A.mro())  # AO
print(X.mro())  # XABO
print(Y.mro())  # YBCO
print(P.mro())  # PXAYBCO