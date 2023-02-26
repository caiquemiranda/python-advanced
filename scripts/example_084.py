# -*- coding: utf-8 -*-
"""
@filename: example_084.py
@author: Caique Miranda
"""
# Example - 084


class Test: 
    def sum(self,*a): 
        total=0 
        for x in a: 
            total=total+x 
            print('The Sum:',total) 

t=Test() 

t.sum(10,20) 
t.sum(10,20,30) 
t.sum(10) 
t.sum()
