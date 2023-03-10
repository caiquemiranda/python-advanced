# -*- coding: utf-8 -*-
"""
@filename: example_034.py
@author: Caique Miranda
"""
# Example - 034


class Employee:

    def __init__(self, eno, ename, esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal

    def display(self):
        print('Employee Number:', self.eno)
        print('Employee Name:', self.ename)
        print('Employee Salary:', self.esal)


class Test:

    def modify(emp):
        emp.esal = emp.esal+10000
        emp.display()


e = Employee(100, 'Durga', 10000)
Test.modify(e)
