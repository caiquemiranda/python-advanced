# -*- coding: utf-8 -*-
"""
@filename: example_078.py
@author: Caique Miranda
"""
# Example - 078


class Book:
    def __init__(self,pages): 
        self.pages=pages 

    def __add__(self,other): 
        return self.pages+other.pages 

b1=Book(100) 
b2=Book(200) 
print('The Total Number of Pages:',b1+b2)