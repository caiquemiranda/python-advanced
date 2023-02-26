# -*- coding: utf-8 -*-
"""
@filename: example_077.py
@author: Caique Miranda
"""
# Example - 077


class Book: 
    def __init__(self,pages): 
        self.pages=pages 

b1=Book(100)
b2=Book(200) 
print(b1+b2)