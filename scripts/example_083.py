# -*- coding: utf-8 -*-
"""
@filename: example_083.py
@author: Caique Miranda
"""
# Example - 083


class Test: 
    def sum(self,a=None,b=None,c=None): 
        if a!=None and b!= None and c!= None: 
            print('The Sum of 3 Numbers:',a+b+c) 
        
        elif a!=None and b!= None: 
            print('The Sum of 2 Numbers:',a+b) 

        else: 
            print('Please provide 2 or 3 arguments') 

t=Test() 
t.sum(10,20) 
t.sum(10,20,30) 
t.sum(10)