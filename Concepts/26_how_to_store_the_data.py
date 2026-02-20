"""
How to store the data

In this section,
1. CLASS VARIABLES
2. INSTANCE VARIABLES
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

print("Store data in all 3 objects")
print("-"*20)
# ---------------

Employee.company_name = "XYZ Company"
Employee.head = "ABC Head"
# Inside object/cubicle 'Employee', 2 variables are getting created
#   1) company_name 2) head

e1.name = "emp-1"
e1.email = "emp-1@someemail.com"
# Inside object/cubicle 'e1', 2 variables are getting created
#   1) name 2) email

e2.name = "emp-2"
e2.email = "emp-2@someemail.com"
e2.phone = "0123456789"
# Inside object/cubicle 'e2', 3 variables are getting created
#   1) name 2) email 3) phone

print("#"*40, end="\n\n")
############################

print("Access data from all 3 objects")
print("-"*20)
# ---------------

print("Company Name:", Employee.company_name)
print("Company Head:", Employee.head, end="\n\n")

print("e1 Name:", e1.name)
print("e1 Company:", e1.company_name)
print("e1.email:", e1.email, end="\n\n")

print("e2 Name:", e2.name)
print("e2 Company:", e2.company_name)
print("e2.email:", e2.email)
print("e2.phone:", e2.phone, end="\n\n")

print("#"*40, end="\n\n")
############################