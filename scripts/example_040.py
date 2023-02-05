# -*- coding: utf-8 -*-
"""
@filename: example_040.py
@author: Caique Miranda
"""
# Example - 040
import time 

class Test: 
    
    def __init__(self): 
        
        print("Constructor Execution...") 
    
    def __del__(self): 
        
        print("Destructor Execution...") 

            
t1=Test() 
t2=t1 
t3=t2 
del t1 
time.sleep(5) 
print("object not yet destroyed after deleting t1")

del t2
time.sleep(5) 

print("object not yet destroyed even after deleting t2")
print("I am trying to delete last reference variable...") 

del t3