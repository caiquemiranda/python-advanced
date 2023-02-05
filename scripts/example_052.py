# -*- coding: utf-8 -*-
"""
@filename: example_052.py
@author: Caique Miranda
"""
# Example - 052


class Student:

    collegeName = 'SUPERPYTHON'

    def __init__(self, name):
        self.name = name
        print(Student.collegeName)


s = Student('Miranda')
print(s.name)
