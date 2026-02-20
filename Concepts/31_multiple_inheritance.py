"""
Using multiple inheritance
"""

print("Writing 'EmployeeClass1' INDEPENDENT CLASS ")
print("-"*20)
# ---------------

class EmployeeClass1:
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

print("Writing 'EmployeeClass2  INDEPENDENT CLASS")
print("-"*20)
# ---------------

class EmployeeClass2:
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

print("Writing 'EmployeeClass3  INDEPENDENT CLASS")
print("-"*20)
# ---------------

class EmployeeClass3:
    @classmethod
    def write_company_details_to_json(cls, json_file_path):
        company_details = {"company_name": cls.company_name, "company_head": cls.company_head}
        my_json_file_handle = open(file=json_file_path, mode="w")
        import json
        json.dump(company_details, my_json_file_handle)
        my_json_file_handle.close()

    @staticmethod # This will take care of NOT passing either INSTANCE or CLASS OBJECT in 1st argument
    def get_company_details_from_json_file(json_file_path):
        my_json_file_handle = open(file=json_file_path, mode="r")
        import json
        company_details = json.load(my_json_file_handle)
        my_json_file_handle.close()
        return company_details

print("#"*40, end="\n\n")
############################

print("Writing 'MasterEmployeeClass' Inheriting from 3 classes")
print("-"*20)
# ---------------

class MasterEmployeeClass(EmployeeClass1, EmployeeClass2, EmployeeClass3):
    """
    Inheriting from more than one class i.e, 3 classes
    """
    #         7. write method to get employee details which is stored inside INSTANCE OBJECT and
    #             get company_name and head which is stored inside CLASS OBJECT. write both
    #             employee details and company details to json file
    def write_employee_company_details_to_json(self, my_class_object, json_file_path):

        # employee_details = {"name": self.name, "email": self.email, "phone": self.phone}
        # OR
        employee_details = self.get_employee_details_from_instance_object()

        # company_details = {"company_name": my_class_object.company_name, "company_head": my_class_object.company_head}
        # OR
        company_details = my_class_object.get_company_details_from_class_object()

        master_data = {"Employee Details": employee_details, "Company Details": company_details}
        my_json_file_handle = open(file=json_file_path, mode="w")
        import json
        json.dump(master_data, my_json_file_handle)
        my_json_file_handle.close()


    # 8. Write method to get employee details and company details from json file
    # -- If we pass json file path then this method will read json file
    #       and return the content. So, inside this method, we don't need
    #       either class object access OR instance object access
    @staticmethod
    def get_employee_company_details_from_json_file(json_file_path):
        my_json_file_handle = open(file=json_file_path, mode="r")
        import json
        employee_company_details = json.load(my_json_file_handle)
        my_json_file_handle.close()
        return employee_company_details

print("#"*40, end="\n\n")
############################

print("Testing 'MasterEmployeeClass':")
print("-"*20)
# ---------------

# Store and get Company Details
MasterEmployeeClass.store_company_details_inside_class_object("XYZ Company", "XYZ Head")
# Internally object 'EmployeeClassRelease2' will be passed to 'cls'
company_details = MasterEmployeeClass.get_company_details_from_class_object()
# Internally object 'EmployeeClassRelease2' will be passed to 'cls'

print("Company details from class object:", company_details, sep="\n", end="\n\n")

# Store and get employee 1 details
e1 = MasterEmployeeClass()
e1.store_employee_details_inside_instance_object("emp-1", "emp-1@someemail.com")
# Internally object 'e1' will be passed to 'self'
employee_details = e1.get_employee_details_from_instance_object()
# Internally object 'e1' will be passed to 'self'
print("Employee 1 Details:", employee_details, sep="\n", end="\n\n")

# Store and get employee 2 details
e2 = MasterEmployeeClass()
e2.store_employee_details_inside_instance_object("emp-2", "emp-2@someemail.com", 123456789)
# Internally object 'e1' will be passed to 'self'
employee_details = e2.get_employee_details_from_instance_object()
# Internally object 'e1' will be passed to 'self'
print("Employee 2 Details:", employee_details, sep="\n", end="\n\n")


MasterEmployeeClass.write_company_details_to_json("company_details.json")
company_details = MasterEmployeeClass.get_company_details_from_json_file("company_details.json")
print("Company details from json file:", company_details, sep="\n", end="\n\n")
print("Created 'company_details.json'", sep="\n", end="\n\n")

e1.write_employee_company_details_to_json(MasterEmployeeClass, "employee_company_details.json")
employee_company_details = MasterEmployeeClass.get_employee_company_details_from_json_file("employee_company_details.json")
print("employee_company_details:", employee_company_details, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
############################