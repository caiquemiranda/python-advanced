# -*- coding: utf-8 -*-
"""
@filename: example_041.py
@author: Caique Miranda
"""
# Example - 041
import time


class Test:

    def __init__(self):
        print("Constructor Execution...")

    def __del__(self):
        print("Destructor Execution...")


list = [Test(), Test(), Test()]
del list
time.sleep(5)
print("End of application")
