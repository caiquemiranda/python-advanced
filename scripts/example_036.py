# -*- coding: utf-8 -*-
"""
@filename: example_036.py
@author: Caique Miranda
"""
# Example - 036


class Person:

    def __init__(self):
        self.name = 'Miranda'
        self.db = self.Dob()

    def display(self):
        print('Name:', self.name)


class Dob:

    def __init__(self):
        self.dd = 10
        self.mm = 5
        self.yy = 1947

    def display(self):
        print(f'Dob={self.dd}/{self.mm}/{self.yy}')


p = Person()
p.display()
x = p.db
x.display()
