"""
Decorator Function: I assume i want to write some 10 functions where
some code is common for all 10 functions. Instead of rewriting common code
in all 10 functions, we can keep that code in 11th function and call that 11th function with all 10 functions

Design Patterns:
https://en.wikipedia.org/wiki/Decorator_pattern
https://en.wikipedia.org/wiki/Software_design_pattern#Structural
"""

print("WITHOUT using decorator function")
print("-"*20)
# ---------------

def add_function(a, b):
    print("Result is:")
    print(a + b)
    print("End of the result", end="\n\n")


def sub_function(a, b):
    print("Result is:")
    print(a - b)
    print("End of the result", end="\n\n")

def mul_function(a, b):
    print("Result is:")
    print(a * b)
    print("End of the result", end="\n\n")

def div_function(a, b):
    print("Result is:")
    print(a / b)
    print("End of the result", end="\n\n")

add_function(10, 20)
sub_function(10, 20)
mul_function(10, 20)
div_function(10, 20)

print("#"*40, end="\n\n")
############################


print("Using Decorator Design Pattern: PARTIALLY IMPLEMENTED HERE")
print("-"*20)
# ---------------

def my_decorator(my_function):
    # def decorated_function(*args, **kwargs):
    def decorated_function(x, y):
        print("Result is:")
        my_function(x, y)
        print("End of the result", end="\n\n")
    return decorated_function

def add_function(a, b):
    print(a + b)

inner_function_reference = my_decorator(add_function)
# 'inner_function_reference' will be having reference to 'decorated_function'
inner_function_reference(10, 20)

def sub_function(a, b):
    print(a - b)

inner_function_reference = my_decorator(sub_function)
# 'inner_function_reference' will be having reference to 'decorated_function'
inner_function_reference(10, 20)

def mul_function(a, b):
    print(a * b)

inner_function_reference = my_decorator(mul_function)
# 'inner_function_reference' will be having reference to 'decorated_function'
inner_function_reference(10, 20)

def div_function(a, b):
    print(a / b)

inner_function_reference = my_decorator(div_function)
# 'inner_function_reference' will be having reference to 'decorated_function'
inner_function_reference(10, 20)

print("#"*40, end="\n\n")
############################

print("Using Decorator Design Pattern: FULLY IMPLEMENTED HERE")
print("-"*20)
# ---------------

def my_decorator(my_function):
    # def decorated_function(*args, **kwargs):
    def decorated_function(x, y):
        print("Result is:")
        my_function(x, y)
        print("End of the result", end="\n\n")
    return decorated_function

@my_decorator
def add_function(a, b):
    print(a + b)

add_function(10, 20)

# @my_decorator will take care of executing below 2 lines
# inner_function_reference = my_decorator(add_function)
# inner_function_reference(10, 20)

@my_decorator
def sub_function(a, b):
    print(a - b)

sub_function(10, 20)

# @my_decorator will take care of executing below 2 lines
# inner_function_reference = my_decorator(sub_function)
# inner_function_reference(10, 20)

@my_decorator
def mul_function(a, b):
    print(a * b)

mul_function(10, 20)

# @my_decorator will take care of executing below 2 lines
# inner_function_reference = my_decorator(mul_function)
# inner_function_reference(10, 20)

@my_decorator
def div_function(a, b):
    print(a / b)

div_function(10, 20)

# @my_decorator will take care of executing below 2 lines
# inner_function_reference = my_decorator(div_function)
# inner_function_reference(10, 20)

print("#"*40, end="\n\n")
############################