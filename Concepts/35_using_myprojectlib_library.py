"""
PACKAGES: If we are developing more modules then we can keep
or organize in folders and subfolders. These folders and subfolders
are called PACKAGES or PYTHON-LIBRARY
"""

print("1-way: using only 'import-statement'")
print("-"*20)
# ---------------

import myprojectlib.db.mymodule
print("Course:", myprojectlib.db.mymodule.course)

add_result = myprojectlib.db.mymodule.add_function(10,20)
print("Add Result:", add_result)

e1=myprojectlib.db.mymodule.Employee("emp-1")
print("Employee Name:", e1.get_name())

print("#"*40, end="\n\n")
############################

print("2-way: using  'from-import-statement'")
print("-"*20)
# ---------------

from myprojectlib.db.mymodule import course, add_function, Employee

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

import myprojectlib.db.mymodule as mm
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

from myprojectlib.db.mymodule import course as c, add_function as af, Employee as E

print("Course:", c)

add_result = af(10,20)
print("Add Result:", add_result)

e1=E("emp-1")
print("Employee Name:", e1.get_name())

print("#"*40, end="\n\n")
############################