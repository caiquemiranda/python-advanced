# -*- coding: utf-8 -*-
"""
@filename: example_054.py
@author: Caique Miranda
"""
# Example - 054


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):

    def __init__(self, name, age, rollno, marks):
        super().__init__(name, age)
        self.rollno = rollno
        self.marks = marks

    def __str__(self):
        return f'Name={self.name}\nAge={self.age}\nRollno={self.rollno}\nMarks={self.marks}'


s1 = Student('Miranda', 48, 101, 90)
print(s1)
