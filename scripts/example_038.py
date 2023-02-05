# -*- coding: utf-8 -*-
"""
@filename: example_038.py
@author: Caique Miranda
"""
# Example - 038
import gc

print(gc.isenabled())
gc.disable()

print(gc.isenabled())
gc.enable()

print(gc.isenabled())
