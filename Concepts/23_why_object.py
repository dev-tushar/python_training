"""
Why Object?

In this section, we need to know 2 terminologies
1) Encapsulation : Keeping data and methods together
2) Abstraction: Purpose of writing methods inside class is to provide ABSTRACTION
    where end user need to know only how to use methods, no need to know
    how each method are implemented.
"""

print("Methods present inside existing class 'str'")
print("-"*20)
# ---------------

print(dir(str))

print("#"*40, end="\n\n")
############################

print("Creating object_1 of type 'str'")
print("-"*20)
# ---------------

object_1 = "Hi"

print("#"*40, end="\n\n")
############################

print("DATA present object_1 of type 'str'")
print("-"*20)
# ---------------

print(object_1)

print("#"*40, end="\n\n")
############################

print("One copy of the methods present in object_1 of type 'str'")
print("-"*20)
# ---------------

print(dir(object_1))

print("#"*40, end="\n\n")
############################

print("Creating object_2 of type 'str'")
print("-"*20)
# ---------------

object_2 = "Hello"

print("#"*40, end="\n\n")
############################

print("DATA present in object_2 of type 'str'")
print("-"*20)
# ---------------

print(object_2)

print("#"*40, end="\n\n")
############################

print("One copy of the methods present in object_2 of type 'str'")
print("-"*20)
# ---------------

print(dir(object_2))

print("#"*40, end="\n\n")
############################