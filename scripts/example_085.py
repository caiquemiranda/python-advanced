# -*- coding: utf-8 -*-
"""
@filename: example_085.py
@author: Caique Miranda
"""
# Example - 085


class Test: 
    def __init__(self): 
        print('No-Arg Constructor')

    def __init__(self,a): 
        print('One-Arg constructor') 

    def __init__(self,a,b): 
        print('Two-Arg constructor') 

#t1=Test() 
#t1=Test(10) 
t1=Test(10,20)