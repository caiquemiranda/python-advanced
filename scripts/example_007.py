# -*- coding: utf-8 -*-
"""
@filename: example_005.py
@author: Caique Miranda
"""
# Example - 007


class Employee:

    def __init__(self):

        self.eno = 100
        self.ename = 'Caique'
        self.esal = 10_000


e = Employee()
print(e.__dict__)
