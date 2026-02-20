"""
How to get objects
- Using class

In this section, We will learn
1. Class object
2. Instance objects
"""

print("Writing our own class")
print("-"*20)
# ---------------

class Employee:
    pass

print("#"*40, end="\n\n")
############################

# ---------------
# About 'pass' keyword
# ---------------
# - To keep any block like if-block, for-block empty
#   then use 'pass'
# - pass is just dummy keyword, so it does nothing
############################

# ---------------
# About 'Employee' class
# ---------------
# - 'Employee' class is empty class
# - Even though 'Employee' class is empty class, it is valid class
# - valid class means,
#   -- we can create objects
#   -- we can store/get data inside each object
#   -- BUT we don't have any methods
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

# ---------------
# Total we have 3 objects
# ---------------
# 1. CLASS OBJECT: By default, in the name of class 'Employee', it will create
#   object and we can use this to store data which is common for all instance objects
# 2. INSTANCE OBJECTS: which we are creating. Here e1 & e2
############################