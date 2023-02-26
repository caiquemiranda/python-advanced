# -*- coding: utf-8 -*-
"""
@filename: example_075.py
@author: Caique Miranda
"""
# Example - 075


class Duck: 
    def talk(self): 
        print('Quack.. Quack..') 

class Dog: 
    def bark(self): 
        print('Bow Bow..') 

def f1(obj): 
    obj.talk() 

d=Duck() 
f1(d) 

d=Dog() 
f1(d)
