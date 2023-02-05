# -*- coding: utf-8 -*-
"""
@filename: example_051.py
@author: Caique Miranda
"""
# Example - 051


class Car:

    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def getinfo(self):
        print(
            f"\tCar Name:{self.name} \n\t Model:{self.model} \n\t Color:{self.color}")


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eatndrink(self):
        print('Eat Biryani and Drink Beer')


class Employee(Person):

    def __init__(self, name, age, eno, esal, car):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal
        self.car = car

    def work(self):
        print("Coding Python is very easy just like drinking Chilled Beer")

    def empinfo(self):
        print("Employee Name:", self.name)
        print("Employee Age:", self.age)
        print("Employee Number:", self.eno)
        print("Employee Salary:", self.esal)
        print("Employee Car Info:")
        self.car.getinfo()


c = Car("Innova", "2.5V", "Grey")
e = Employee('Miranda', 48, 100, 10000, c)
e.eatndrink()
e.work()
e.empinfo()
