"""
In this program, we are providing implementation for below methods
3. write method to store employee details inside INSTANCE OBJECT
4. write method to get employee details which is stored inside INSTANCE OBJECT
"""

print("Writing 'EmployeeClassRelease1")
print("-"*20)
# ---------------

class EmployeeClassRelease1:
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

# ---------------
# About 'Inheritance'
# ---------------
# - If we want to add some functionalities/methods to existing class
#   which is already released then instead of modifying existing class
#   we can extend existing class and create new class. In new class add
#   new functionalities/methods. Automatically existing class functionalities/methods
#   will come to our new class. So, our new class will be having both
#   existing class functionalities/methods and new class functionalities/methods.
############################

print("Writing 'EmployeeClassRelease2")
print("-"*20)
# ---------------

# To add 2 more methods, we are extending 'EmployeeClassRelease1"
# and creating new class 'EmployeeClassRelease2". Now automatically
# whatever there in ''EmployeeClassRelease1" will come to 'EmployeeClassRelease2"

class EmployeeClassRelease2(EmployeeClassRelease1):
    """
    we are providing implementation for below methods
        3. write method to store employee details inside INSTANCE OBJECT
        4. write method to get employee details which is stored inside INSTANCE OBJECT
    """
    def store_employee_details_inside_instance_object(self, name, email, phone=None):
        self.name = name
        self.email = email
        self.phone = phone

    def get_employee_details_from_instance_object(self):
        employee_details = {"name": self.name, "email": self.email, "phone": self.phone}
        return employee_details

print("#"*40, end="\n\n")
############################

print("Testing 'EmployeeClassRelease2':")
print("-"*20)
# ---------------

# Store and get Company Details
EmployeeClassRelease2.store_company_details_inside_class_object("XYZ Company", "XYZ Head")
# Internally object 'EmployeeClassRelease2' will be passed to 'cls'
company_details = EmployeeClassRelease2.get_company_details_from_class_object()
# Internally object 'EmployeeClassRelease2' will be passed to 'cls'

print("Company details:", company_details)

# Store and get employee 1 details
e1 = EmployeeClassRelease2()
e1.store_employee_details_inside_instance_object("emp-1", "emp-1@someemail.com")
# Internally object 'e1' will be passed to 'self'
employee_details = e1.get_employee_details_from_instance_object()
# Internally object 'e1' will be passed to 'self'
print("Employee 1 Details:", employee_details)

# Store and get employee 2 details
e2 = EmployeeClassRelease2()
e2.store_employee_details_inside_instance_object("emp-2", "emp-2@someemail.com")
# Internally object 'e1' will be passed to 'self'
employee_details = e2.get_employee_details_from_instance_object()
# Internally object 'e1' will be passed to 'self'
print("Employee 2 Details:", employee_details)


print("#"*40, end="\n\n")
############################