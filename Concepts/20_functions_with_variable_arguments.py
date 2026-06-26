"""
Functions with variable arguments
- Functions with variable POSITIONAL arguments
- Functions with variable KEYWORD arguments
"""
print("Functions with variable POSITIONAL arguments")
print("-"*20)
# ---------------

# *a : is called VARIABLE POSITIONAL ARGUMENTS
def add(*a):  #0 or more positional arguments can be given like shown below
    print("Received all values in tuple 'a':", a)
    total = sum(a)
    return total

add_result = add()
print("add_result:", add_result)

add_result = add(10)
print("add_result:", add_result)

add_result = add(10, 20, 30, 40)
print("add_result:", add_result)

print("#"*40, end="\n\n")
############################


print("Functions with variable KEYWORD arguments")
print("-"*20)
# ---------------

#  **employee_info : is called VARIABLE KEYWORD ARGUMENTS

def employee_profile(**employee_info):
    print("Received all values in dictionary 'employee_info':", employee_info)
    if len(employee_info) > 0:
        file_name = employee_info["name"] + ".json"
        my_file_handle =open(file=file_name, mode="w")
        import json
        json.dump(employee_info, my_file_handle)
        my_file_handle.close()



employee_profile()
employee_profile(name="emp-1")
employee_profile(name="emp-2", company="comp-2")
employee_profile(name="emp-3", company="comp-3", email="emp-3@comp3")
print("""Created below files
emp-1.json
emp-2.json
emp-3.json
""")

print("#"*40, end="\n\n")
############################