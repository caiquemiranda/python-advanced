# -*- coding: utf-8 -*-
"""
@filename: example_090.py
@author: Caique Miranda
"""
# Example - 090


class P: 
    def __init__(self): 
        print('Parent Constructor') 

class C(P): 
    def __init__(self): 
        print('Child Constructor') 

c=C()