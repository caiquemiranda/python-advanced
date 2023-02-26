# -*- coding: utf-8 -*-
"""
@filename: example_080.py
@author: Caique Miranda
"""
# Example - 080


class Employee: 
    def __init__(self,name,salary): 
        self.name=name 
        self.salary=salary 

    def __mul__(self,other): 
        return self.salary*other.days
    
class TimeSheet: 
    def __init__(self,name,days): 
        self.name=name 
        self.days=days 

e=Employee('Miranda',500) 
t=TimeSheet('Miranda',25) 

print('This Month Salary:',e*t)