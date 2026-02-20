"""
2 Cases we are planning

Case-1: How to access values outside the functions
    - Called, Functions with return values

Case-2: How to pass values to variables present inside the function
    - Called, Functions with arguments

In this program, we are discussing on
Case-1: How to access values outside the functions
    - Called, Functions with return values
"""
print("Function with SINGLE return value")
print("-"*20)
# ---------------

# 2 steps to return values
# step-1: inside function, use 'return-statement' to specify list of values to send outside the function
# step-2: while calling the function, assign function call to some variable so that returned value will be
#           stored in that variable

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # step-1: inside function, use 'return-statement' to specify list of values to send outside the function
    return name


# step-2: while calling the function, assign function call to some variable so that returned value will be
#           stored in that variable
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
############################

print("Function with returning MULTIPLE values: TUPLE")
print("-"*20)
# ---------------

# 2 steps to return values
# step-1: inside function, use 'return-statement' to specify list of values to send outside the function
# step-2: while calling the function, assign function call to some variable so that returned value will be
#           stored in that variable

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # step-1: inside function, use 'return-statement' to specify list of values to send outside the function
    return (name, company)


# step-2: while calling the function, assign function call to some variable so that returned value will be
#           stored in that variable
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
############################

print("Function with returning MULTIPLE values: DICTIONARY")
print("-"*20)
# ---------------

# 2 steps to return values
# step-1: inside function, use 'return-statement' to specify list of values to send outside the function
# step-2: while calling the function, assign function call to some variable so that returned value will be
#           stored in that variable

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # step-1: inside function, use 'return-statement' to specify list of values to send outside the function
    return {"name": name, "company": company}


# step-2: while calling the function, assign function call to some variable so that returned value will be
#           stored in that variable
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
############################