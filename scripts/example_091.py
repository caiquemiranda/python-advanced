# -*- coding: utf-8 -*-
"""
@filename: example_091.py
@author: Caique Miranda
"""
# Example - 091


class Person: 
    def __init__(self,name,age): 
        self.name=name 
        self.age=age 

class Employee(Person): 
    def __init__(self,name,age,eno,esal): 
        super().__init__(name,age)
        self.eno=eno 
        self.esal=esal 

    def display(self): 
        print('Employee Name:',self.name) 
        print('Employee Age:',self.age) 
        print('Employee Number:',self.eno) 
        print('Employee Salary:',self.esal) 

e1=Employee('Miranda',48,872425,26000) 
e1.display()

e2=Employee('Santos',39,872426,36000) 
e2.display()