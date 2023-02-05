# -*- coding: utf-8 -*-
"""
@filename: example_005.py
@author: Caique Miranda
"""
# Example - 006


class Student:
    ''''' This is student class with required data'''

    def __init__(self, name, rollno, marks):

        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display(self):

        print(
            f"Student Name:{self.name}\nRollno:{self.rollno} \nMarks:{self.marks}")


s1 = Student("Caique", 101, 80)
s1.display()

s2 = Student("Santos", 102, 100)
s2.display()
