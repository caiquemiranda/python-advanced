# -*- coding: utf-8 -*-
"""
@filename: example_037.py
@author: Caique Miranda
"""
# Example - 037


class Human:

    def __init__(self):

        self.name = 'Lancy'
        self.head = self.Head()
        self.brain = self.Brain()

    def display(self):

        print("Hello..", self.name)


class Head:

    def talk(self):

        print('Talking...')


class Brain:

    def think(self):
        print('Thinking...')


h = Human()
h.display()
h.head.talk()
h.brain.think()
