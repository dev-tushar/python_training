"""
Numbers: We already have option to store numbers like 10, 12,5 in a variables
"""
print("Number Example:")
# print("-------------")
print("-"*20) # string repetation. repeat "-" into 20 times
# ---------------

a = 10
# internally, it will create object of builtin class 'int' and store the value 10 inside that object
b = 12.5
# internally, it will create object of builtin class 'float' and store the value 12.5 inside that object
c = a + b
# internally, it will create object of builtin class 'float' and store the value 22.5 inside that object
print("Value of a is:", a)
print("Value of b is:", b)
print("Value of c is:", c)

print("#"*40, end="\n\n")
# default end="\n" which means, after printing put one \n(newline) at the end
# end="\n\n". Put two \n at the end of the print
############################