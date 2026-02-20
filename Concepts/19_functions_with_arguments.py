"""
Here,
Case-2: How to pass values to variables present inside the function
    - Called, Functions with arguments

3 ways we can pass values to variables present inside the function

1-way: we can either pass only values OR we can also specify both 'argument name and value'
    - Called, Functions with POSITIONAL or KEYWORD arguments

2-way: we can RESTRICT to  pass only values
    - Called, Functions with ONLY POSITIONAL arguments

3-way: we can RESTRICT to specify both 'argument name and value'
    - Called, Functions with ONLY KEYWORD arguments
"""

print("""
1-way: we can either pass only values OR we can also specify both 'argument name and value'
    - Called, Functions with POSITIONAL or KEYWORD arguments
""")
print("-"*20)
# ---------------

# name, company are called POSITIONAL or KEYWORD arguments
def employee(name, company):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}

# OPTION-1: We can pass only values
received_value = employee("emp-1", "comp-1")
print("received_value:", received_value)

# OPTION-2: we can also specify both 'argument name and value'
received_value = employee(name="emp-1", company="comp-1")
print("received_value:", received_value)

print("#"*40, end="\n\n")
############################

print("""
2-way: we can RESTRICT to  pass only values
    - Called, Functions with ONLY POSITIONAL arguments
""")
print("-"*20)
# ---------------

# / - > is just syntax to tell it is ONLY POSITIONAL arguments
# / -> is not counted as an argument
# / -> for /, we are not passing any values
# / -> so, below function is having only 2 arguments name & company. NOT 3 arguments

# name, company are called ONLY POSITIONAL arguments
def employee(name, company, /):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}

# OPTION-1: We can pass only values
received_value = employee("emp-1", "comp-1")
print("received_value:", received_value)

# OPTION-2 will not work here

# OPTION-2: we can also specify both 'argument name and value'
# received_value = employee(name="emp-1", company="comp-1")
# print("received_value:", received_value)

print("#"*40, end="\n\n")
############################

print("""
3-way: we can RESTRICT to specify both 'argument name and value'
    - Called, Functions with ONLY KEYWORD arguments
""")
print("-"*20)
# ---------------

# * - > is just syntax to tell it is ONLY KEYWORD arguments
# * -> is not counted as an argument
# * -> for *, we are not passing any values
# * -> so, below function is having only 2 arguments name & company. NOT 3 arguments

# name, company are called ONLY KEYWORD arguments
def employee(*, name, company):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}

# OPTION-1 will not work here

# OPTION-1: We can pass only values
# received_value = employee("emp-1", "comp-1")
# print("received_value:", received_value)

# OPTION-2: we can also specify both 'argument name and value'
received_value = employee(name="emp-1", company="comp-1")
print("received_value:", received_value)

print("#"*40, end="\n\n")
############################