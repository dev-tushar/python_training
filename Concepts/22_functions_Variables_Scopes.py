"""
Variable Scopes
1. Local scope
2. Enclosed Scope
3. Global Scope
4. Builtin scope:
"""

print("1. Local scope: Example")
print("-"*20)
# ---------------

def my_function():
    x = 100 # This is LOCAL scope, so we can access within this function only
    print("Value of x is:", x)

my_function()

print("#"*40, end="\n\n")
############################

print("2. Enclosed Scope: Example")
print("-"*20)
# ---------------

def my_function_1():
    y = 100 # This variable can be accessed by CURRENT and NESTED function
    def my_function_2():
        nonlocal y # nonlocal will refer outer function variable
        print("Value of outer function y is:", y)
    my_function_2()
my_function_1()

print("#"*40, end="\n\n")
############################

print("3. Global Scope Example")
print("-"*20)
# ---------------

z = 100
def my_function_1():
    global z
    print("Value of z in my_function_1 is:", z)
    def my_function_2():
        global z
        print("Value of z in my_function_2 is:", z)
    my_function_2()
my_function_1()

print("#"*40, end="\n\n")
############################

# ---------------
#  Builtin scope:
# ---------------
#  If not found in local, enclosed, global then it will check in builtins.
# If not present in builtins then it will throw ERROR
############################