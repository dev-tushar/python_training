"""
In this program, we are providing implementation for below methods
5. Write method to get company details from CLASS OBJECT and write to json file
6. Write method to get company details from json file

We are using multilevel inheritance to take methods from existing classes
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

print("Writing 'EmployeeClassRelease3")
print("-"*20)
# ---------------

class EmployeeClassRelease3(EmployeeClassRelease2):
    """
    we are providing implementation for below methods
    5. Write method to get company details from CLASS OBJECT and write to json file
    6. Write method to get company details from json file
    """

    # 5. Write method to get company details from CLASS OBJECT and write to json file
    # -- Since we need to get company details from class object, this method requires
    #       CLASS OBJECT access inside the method so we need to pass CLASS OBJECT to this method
    @classmethod
    def write_company_details_to_json(cls, json_file_path):
        company_details = {"company_name": cls.company_name, "company_head": cls.company_head}
        my_json_file_handle = open(file=json_file_path, mode="w")
        import json
        json.dump(company_details, my_json_file_handle)
        my_json_file_handle.close()

    # 6. Write method to get company details from json file
    # -- If we pass json file path then this method will read json file
    #       and return the content. So, inside this method, we don't need
    #       either class object access OR instance object access
    @staticmethod # This will take care of NOT passing either INSTANCE or CLASS OBJECT in 1st argument
    def get_company_details_from_json_file(json_file_path):
        my_json_file_handle = open(file=json_file_path, mode="r")
        import json
        company_details = json.load(my_json_file_handle)
        my_json_file_handle.close()
        return company_details


print("#"*40, end="\n\n")
############################

print("Testing 'EmployeeClassRelease3':")
print("-"*20)
# ---------------

# Store and get Company Details
EmployeeClassRelease3.store_company_details_inside_class_object("XYZ Company", "XYZ Head")
# Internally object 'EmployeeClassRelease2' will be passed to 'cls'
company_details = EmployeeClassRelease3.get_company_details_from_class_object()
# Internally object 'EmployeeClassRelease2' will be passed to 'cls'

print("Company details from class object:", company_details, sep="\n", end="\n\n")

# Store and get employee 1 details
e1 = EmployeeClassRelease3()
e1.store_employee_details_inside_instance_object("emp-1", "emp-1@someemail.com")
# Internally object 'e1' will be passed to 'self'
employee_details = e1.get_employee_details_from_instance_object()
# Internally object 'e1' will be passed to 'self'
print("Employee 1 Details:", employee_details, sep="\n", end="\n\n")

# Store and get employee 2 details
e2 = EmployeeClassRelease3()
e2.store_employee_details_inside_instance_object("emp-2", "emp-2@someemail.com", 123456789)
# Internally object 'e1' will be passed to 'self'
employee_details = e2.get_employee_details_from_instance_object()
# Internally object 'e1' will be passed to 'self'
print("Employee 2 Details:", employee_details, sep="\n", end="\n\n")


EmployeeClassRelease3.write_company_details_to_json("company_details.json")
company_details = EmployeeClassRelease3.get_company_details_from_json_file("company_details.json")
print("Company details from json file:", company_details, sep="\n", end="\n\n")
print("Created 'company_details.json'", sep="\n", end="\n\n")

print("#"*40, end="\n\n")
############################