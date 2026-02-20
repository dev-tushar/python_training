"""
We will check what is present in each object which we create.
"""
print("Writing our own class")
print("-"*20)
# ---------------

class Employee:
    pass

print("#"*40, end="\n\n")
############################

print("Create 2 objects")
print("-"*20)
# ---------------

e1 = Employee()
# It will create object and store in e1
e2 = Employee()
# It will create another object and store in e2

print("#"*40, end="\n\n")
############################

print('DATA present in each object')
print("-"*20)
# ---------------

print("DATA present in each CLASS OBJECT 'Employee':", Employee)
print("DATA present in each INSTANCE OBJECT 'e1':", e1)
print("DATA present in each INSTANCE OBJECT 'e2':", e2)

print("#"*40, end="\n\n")
############################

print('METHODS present in each object')
print("-"*20)
# ---------------

print("METHODS present in each CLASS OBJECT 'Employee':", dir(Employee), sep="\n", end="\n\n")
print("METHODS present in each INSTANCE OBJECT 'e1':", dir(e1), sep="\n", end="\n\n")
print("METHODS present in each INSTANCE OBJECT 'e2':",  dir(e2), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
############################

# ---------------
# About 'object' class
# ---------------
# - 'object' class is 1st class in python
# - 'object' class is having basic functionalities/methods required
#   for each and every class to work
#   like constructor __new__, initializer __init__
# - Whenever we create new class, automatically whatever there in
#   'object' class will come to our new class. This is called INHERITANCE
############################