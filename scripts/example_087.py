# -*- coding: utf-8 -*-
"""
@filename: example_087.py
@author: Caique Miranda
"""
# Example - 087


class Test: 
    def __init__(self,*a):      
        print('Constructor with variable number of arguments') 

t1=Test() 
t2=Test(10) 
t3=Test(10,20) 
t4=Test(10,20,30) 
t5=Test(10,20,30,40,50,60)