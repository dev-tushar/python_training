"""
In this file, we are keeping
- all variables
- all functions
- all classes
which we are planning to use it in other programs

This file is also called as PYTHON-MODULE or PYTHON-LIBRARY
"""

course = "Python"

def add_function(a, b):
    return a + b

class Employee:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name