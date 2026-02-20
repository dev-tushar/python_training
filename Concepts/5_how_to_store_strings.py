"""
Strings:  We already have option to store text data like name, email-id, address, -word, sentence, paragraphs
        - Automatically index number will be assigned to each and every character
"""
from operator import indexOf

print("Strings PART-1:")
print("How to store values")
print("-"*20)
# ---------------

a = 'PERSON'
b = "PERSON'S"
c = """PERSON'S HEIGHT IS XYZ" (" represents inch)"""
d = '''PERSON'S HEIGHT IS XYZ" (" represents inch)'''
e = 'PERSON\'S'

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

print(a,b,c,d,e, sep="\n")
# sep -> is one parameter to print() function
# default sep is ONE SPACE, which means, in output put one-space between each value
# sep="\n", in output put one-newline between each value


print("#"*40, end="\n\n")
############################

print("Strings PART-2:")
print("How to store values")
print("-"*20)
# ---------------

my_file_path_1 = "C:\newfolder\test.py"
print("my_file_path_1:", my_file_path_1, end="\n\n")
# Few characters along with \,
# being used for special purpose
# Example: \n -> to put newline, \t -> to put tab space

my_file_path_2 = r"C:\newfolder\test.py"
print("my_file_path_2 in raw format:", my_file_path_2, end="\n\n")
# r -> raw format of the string when \n\t etc are ignored as special delimiters
# and considered as string

my_file_path_3 = repr(my_file_path_1) # Convert any string into raw format
print("my_file_path_1 in raw format is my_file_path_3:", my_file_path_3, end="\n\n")
# repr -> convert to raw format of the string

print("#"*40, end="\n\n")
############################

print("Strings PART-3:")
print("How to store values")
print("-"*20)
# ---------------

a = 10
b = 20
my_string = f"Value of a is {a} and value of b is {b}"
# f-> format
# f -> it will replace {variable_name} with variable_value

print("my_string using format 'f':", my_string, end="\n\n")

print("#"*40, end="\n\n")
############################


print("Strings PART-4:")
print("Automatically index number will be assigned to each and every character")
print("We can do 4 things using that index number")
print("1-thing we can do with that index number is: We can access individual characters")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer example-1 in 6_strings.xlsx

print("0th character using positive index number:", my_string[0])
print("0th character using negative index number:", my_string[-8], end="\n\n")

# print("100th character using positive index number:", my_string[100])
# ERROR

print("#"*40, end="\n\n")
############################

print("Strings PART-5:")
print("Automatically index number will be assigned to each and every character")
print("We can do 4 things using that index number")
print("2nd-thing we can do with that index number is: We can get substring")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer example-2 in 6_strings.xlsx

print("substring from index-1 to index-6 using positive index number:", my_string[1:6])
print("substring from index-1 to index-6 using negative index number:", my_string[-7:-2])
# Here, character at start index will be included in the substring
# Here, character at end index will be EXCLUDED in the substring
# So, if we want chatarcter at index-6 then we need to specify 7 as end index

print("#"*40, end="\n\n")
############################

print("Strings PART-6:")
print("Automatically index number will be assigned to each and every character")
print("We can do 4 things using that index number")
print("3rd-thing we can do with that index number is: We can skip characters")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer example-3 in 6_strings.xlsx
print("substring from index-1 to index-6 using positive index number with default step value=1:", my_string[1:6])
print("substring from index-1 to index-6 using negative index number with default step value=1:", my_string[-7:-2], end="\n\n")
# step=1: which means, from index-1 to index-6, give me every character

print("substring from index-1 to index-6 using positive index number with step value=1:", my_string[1:6:1])
print("substring from index-1 to index-6 using negative index number with step value=1:", my_string[-7:-2:1], end="\n\n")
# step=1: which means, from index-1 to index-6, give me every character

print("substring from index-1 to index-6 using positive index number with step value=2:", my_string[1:6:2])
print("substring from index-1 to index-6 using negative index number with step value=2:", my_string[-7:-2:2], end="\n\n")
# step=2: which means, from index-1 to index-6, give me every second character

print("substring from index-1 to index-6 using positive index number with step value=3:", my_string[1:6:3])
print("substring from index-1 to index-6 using negative index number with step value=3:", my_string[-7:-2:3], end="\n\n")
# step=3: which means, from index-1 to index-6, give me every third character

print("#"*40, end="\n\n")
############################


print("Strings PART-7:")
print("Automatically index number will be assigned to each and every character")
print("We can do 4 things using that index number")
print("4th-thing we can do with that index number is: We can traverse in reverse order")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer example-4 in 6_strings.xlsx

# To traverse in reverse direction,
#
# Example: get substring from index-6 to index-1
#
# we need to follow below 3 steps
# Step-1: start index should be index-6
# Step-2: end index should be index-1
# Step-3: step value should be negative
# If we miss any of the step then we will get substring

print("substring from index 6 to index 1 using positive index number with step value=-1:", my_string[6:1:-1])
print("substring from index 6 to index 1 using negative index number with step value=-1:", my_string[-2:-7:-1])

print("substring from index-6 to index-1 using positive index number with step value=-2:", my_string[6:1:-2])
print("substring from index-6 to index-1 using negative index number with step value=-2:", my_string[-2:-7:-2])

print("#"*40, end="\n\n")
############################

print("Strings PART-8:")
print("List of methods present in str class")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

print(dir(str))
# OR
print(dir(my_string))

print("#"*40, end="\n\n")
############################

print("Strings PART-9:")
print("DATA present in string class object 'cubicle_1'")
print("-"*20)
# ---------------

cubicle_1 = "Hi"
print(cubicle_1)

print("#"*40, end="\n\n")
############################

print("Strings PART-10:")
print("One copy of str class METHODS present in string class object 'cubicle_1'")
print("-"*20)
# ---------------

print(dir(cubicle_1))

print("#"*40, end="\n\n")
############################


print("Strings PART-11:")
print("DATA present in string class object 'cubicle_2'")
print("-"*20)
# ---------------

cubicle_2 = "Hello"
print(cubicle_2)

print("#"*40, end="\n\n")
############################

print("Strings PART-12:")
print("One copy of str class METHODS present in string class object 'cubicle_2'")
print("-"*20)
# ---------------

print(dir(cubicle_2))

print("#"*40, end="\n\n")
############################

print("Strings PART-13")
print("Learning capitalize() method")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string", my_string, end="\n\n")

capitalized_string = my_string.capitalize()
print("capitalized_string", capitalized_string, end="\n\n")

#############################
print("#"*40, end="\n\n")

#Skipping space from string 'WEL COME'

print("Strings PART-14")
origStr = "WEL COME"
print(origStr, end="\n\n")

newStr = origStr.replace(" ","").capitalize()
#print(newStr.capitalize(), end="\n\n")

print(f"Proper string is {newStr}", end="\n\n")

if " " in origStr:
        indexSpace = indexOf(origStr, " ")
StrPart1 = origStr[0:indexSpace]
StrPart2 = origStr[indexSpace+1:]
conCatStr = (StrPart1+StrPart2).capitalize()
print(f"Concatenated string is: {conCatStr}")