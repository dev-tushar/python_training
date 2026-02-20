"""
About __ double underscore names

1. Few __ names are using by super class 'object' for methods like
        __new__ for constructor
        , __init__ for initializer

2. Few __ names are used for all operators like +, - etc

3. Few __names are used for some builtin functions like len()

"""

"""
We can always rewrite methods with the same name (POLYMORPHISM) 
which is coming from super-class
- This is called METHOD OVERRIDING
"""

print("Writing class to store/get employee name")
print("-"*20)
# ---------------

class Employee:
    def store_name(self, name):
        self.name = name
    def get_name(self):
        return self.name

e1 = Employee()
e1.store_name("emp-1")
print("Name:", e1.get_name())

print("#"*40, end="\n\n")
############################

print("Writing class to store/get employee name overriding __init__ for storing name")
print("-"*20)
# ---------------

class Employee:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name

e1 = Employee("emp-1") # __init__('emp-1')
# e1.store_name("emp-1")
print("Name:", e1.get_name())

print("#"*40, end="\n\n")
############################

print("Supporting +")
print("-"*20)
# ---------------

class Employee:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def __add__(self, other):
        return self.name + other.name


e1 = Employee("emp-1") # __init__('emp-1')
print("Name:", e1.get_name())
e2 = Employee("emp-2") # __init__('emp-2')
print("Name:", e2.get_name())

add_result = e1 + e2 # e1.__add__(e2)
print("add_result:", add_result)

print("#"*40, end="\n\n")
############################

print("Supporting len()")
print("-"*20)
# ---------------

class Employee:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)


e1 = Employee("emp-1") # __init__('emp-1')
print("Name:", e1.get_name())
e2 = Employee("emp-2") # __init__('emp-2')
print("Name:", e2.get_name(), end="\n\n")

add_result = e1 + e2 # e1.__add__(e2)
print("add_result using +:", add_result, end="\n\n")

print("Length of 'e1':", len(e1))
print("Length of 'e2':", len(e2), end="\n\n")

print("#"*40, end="\n\n")
############################