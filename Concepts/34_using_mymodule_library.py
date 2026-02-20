"""
This program, we are accessing
- Variables
- Functions
- Classes
present in mymodule library
"""
print("1-way: using only 'import-statement'")
print("-"*20)
# ---------------

import mymodule
print("Course:", mymodule.course)

add_result = mymodule.add_function(10,20)
print("Add Result:", add_result)

e1=mymodule.Employee("emp-1")
print("Employee Name:", e1.get_name())

print("#"*40, end="\n\n")
############################

print("2-way: using  'from-import-statement'")
print("-"*20)
# ---------------

from mymodule import course, add_function, Employee

print("Course:", course)

add_result = add_function(10,20)
print("Add Result:", add_result)

e1=Employee("emp-1")
print("Employee Name:", e1.get_name())

print("#"*40, end="\n\n")
############################

print("WITH SHORT NAME: 1-way: using only 'import-statement'")
print("-"*20)
# ---------------

import mymodule as mm
print("Course:", mm.course)

add_result = mm.add_function(10,20)
print("Add Result:", add_result)

e1=mm.Employee("emp-1")
print("Employee Name:", e1.get_name())

print("#"*40, end="\n\n")
############################

print("WITH SHORT NAME: 2-way: using  'from-import-statement'")
print("-"*20)
# ---------------

from mymodule import course as c, add_function as af, Employee as E

print("Course:", c)

add_result = af(10,20)
print("Add Result:", add_result)

e1=E("emp-1")
print("Employee Name:", e1.get_name())

print("#"*40, end="\n\n")
############################