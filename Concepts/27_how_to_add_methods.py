"""
How to add methods
"""

"""
Requirement:
1. Write method to store company_name and head inside CLASS OBJECT
2. Write method to get company_name and head which is stored inside CLASS OBJECT
3. write method to store employee details inside INSTANCE OBJECT
4. write method to get employee details which is stored inside INSTANCE OBJECT
5. Write method to get company details from CLASS OBJECT and write to json file
6. Write method to get company details from json file 
7. write method to get employee details which is stored inside INSTANCE OBJECT and
    get company_name and head which is stored inside CLASS OBJECT. write both
    employee details and company details to json file
8. Write method to get employee details and company details from json file 
"""



"""
In this program, we are implementing below methods
1. Write method to store company_name and head inside CLASS OBJECT
2. Write method to get company_name and head which is stored inside CLASS OBJECT
"""

print("Writing 'Employee' class")
print("-"*20)
# ---------------

class Employee:
    @classmethod
    def store_company_details_inside_class_object(cls, company_name, company_head):
        cls.company_name = company_name
        cls.company_head = company_head

    @classmethod
    def get_company_details_from_class_object(cls):
        company_details = {"company_name": cls.company_name, "company_head": cls.company_head}
        return company_details

print("#"*40, end="\n\n")
############################

print("Testing 'Employee' class")
print("-" * 20)
# ---------------
# point-1: No need to create instance object here. Because our requirement
# required class object 'Employee' which is automatically getting created

Employee.store_company_details_inside_class_object("XYZ company", "XYZ Head")
# Internally class object 'Employee' will be passed to 1st argument 'cls'

company_details = Employee.get_company_details_from_class_object()
# Internally class object 'Employee' will be passed to 1st argument 'cls'
print(company_details)

print("#" * 40, end="\n\n")
############################

# ---------------
# About '@classmethod'
# ---------------
# - @classmethod is one type of function called 'DECORATOR'
# - use of decorator is, we can attach functionality present in @classmethod
#   to any function
# - So, we need to write @classmethod exactly on top of function definition
# - In @classmethod, we have functionality which take care of ALWAYS passing
#   class object to 'cls' even though if we call that method using any instance objects like
#   e1, e2, which we created in previous program
############################