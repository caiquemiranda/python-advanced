# -*- coding: utf-8 -*-
"""
@filename: example_039.py
@author: Caique Miranda
"""
# Example - 039
import time


class Test:

    def __init__(self):
        print("Object Initialization...")

    def __del__(self):
        print("Fulfilling Last Wish and performing clean up activities...")


t1 = Test()
t1 = None
time.sleep(5)
print("End of application")
