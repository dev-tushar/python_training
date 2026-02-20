"""
Conditional statement 'if' statement:
"""
print("Using only 'if-block':")
print("-"*20)
# ---------------

x = 10
if (x == 10) and (x < 100):
    print("x is equal to 10: line-1")
    print("x is equal to 10: line-2")
    print("x is equal to 10: line-3")
    print("x is equal to 10: line-4")
    print("x is equal to 10: line-5")
if x > 10:
    print("x is greater than 10: line-1")
    print("x is greater than 10: line-2")
    print("x is greater than 10: line-3")
    print("x is greater than 10: line-4")
    print("x is greater than 10: line-5")
if x < 10:
    print("x is less than 10: line-1")
    print("x is less than 10: line-2")
    print("x is less than 10: line-3")
    print("x is less than 10: line-4")
    print("x is less than 10: line-5")

print("#"*40, end="\n\n")
############################

print("Using only 'if-elif-block':")
print("-"*20)
# ---------------

x = 10
if (x == 10) and (x < 100):
    print("x is equal to 10: line-1")
    print("x is equal to 10: line-2")
    print("x is equal to 10: line-3")
    print("x is equal to 10: line-4")
    print("x is equal to 10: line-5")
elif x > 10:
    print("x is greater than 10: line-1")
    print("x is greater than 10: line-2")
    print("x is greater than 10: line-3")
    print("x is greater than 10: line-4")
    print("x is greater than 10: line-5")
elif x < 10:
    print("x is less than 10: line-1")
    print("x is less than 10: line-2")
    print("x is less than 10: line-3")
    print("x is less than 10: line-4")
    print("x is less than 10: line-5")

print("#"*40, end="\n\n")
############################

print("Using 'if-elif-else block':")
print("-"*20)
# ---------------

x = 10
if (x == 10) and (x < 100):
    print("x is equal to 10: line-1")
    print("x is equal to 10: line-2")
    print("x is equal to 10: line-3")
    print("x is equal to 10: line-4")
    print("x is equal to 10: line-5")
elif x > 10:
    print("x is greater than 10: line-1")
    print("x is greater than 10: line-2")
    print("x is greater than 10: line-3")
    print("x is greater than 10: line-4")
    print("x is greater than 10: line-5")
else:
    print("x is less than 10: line-1")
    print("x is less than 10: line-2")
    print("x is less than 10: line-3")
    print("x is less than 10: line-4")
    print("x is less than 10: line-5")

print("#"*40, end="\n\n")
############################


print("Using 'if block' with string, list, tuple etc:")
print("-"*20)
# ---------------

my_string = "Python"
print("my_string: ",  my_string, end="\n\n")

if "th" in my_string:
    print("substring 'th' found in my_string")

my_list = ["emp-1", "emp-2", "emp-3"]
print("my_list: ", my_list, end="\n\n")

if "emp-2" in my_list:
    print("Employee name 'emp-2' found in my_list")

print("#"*40, end="\n\n")
############################