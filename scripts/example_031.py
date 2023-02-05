# -*- coding: utf-8 -*-
"""
@filename: example_031.py
@author: Caique Miranda
"""
# Example - 031


class Animal:
    lEgs = 4

    @classmethod
    def walk(cls, name):
        print('{} walks with {} lEgs...'.format(name, cls.lEgs))


Animal.walk('Dog')
Animal.walk('Cat')
