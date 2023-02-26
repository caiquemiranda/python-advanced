# -*- coding: utf-8 -*-
"""
@filename: example_082.py
@author: Caique Miranda
"""
# Example - 082


class Test: 
    def m1(self): 
        print('no-arg method') 

    def m1(self,a): 
        print('one-arg method') 

    def m1(self,a,b): 
        print('two-arg method') 

t=Test() 
#t.m1() 
t.m1(10) 
t.m1(10,20)