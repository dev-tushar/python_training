"""
for-loop: iterate any collection like string, list, tuple etc
"""

print("for-loop with strings")
print("-"*20)
# ---------------

my_string = "Python"
print("my_string", my_string, end="\n\n")

for i in my_string:
    print("Character stored in variable 'i' is:", i)

print("#"*40, end="\n\n")
############################


print("for-loop with list/tuple")
print("-"*20)
# ---------------

my_list = ["emp-1", "emp-2", "emp-3", "emp-4"]
print("my_list", my_list, end="\n\n")

for j in my_list:
    print("Value stored in variable 'j' is:", j)

print("#"*40, end="\n\n")
############################


print("for-loop with Dictionary")
print("-"*20)
# ---------------

my_dictionary = {
    "duration": 10,
     "course": "python",
     "mode": ["online", "offline"],
     "trainer": {"fname": "abc", "lname": "xyz"}
     }
print("my_dictionary:", my_dictionary, end="\n\n")

for k in my_dictionary: # Iterate keys
    print("Key stored in variable 'k' is:", k)
    print("Value is:", my_dictionary[k])

print("#"*40, end="\n\n")
############################

print("manually end for-loop using 'break' statement")
print("-"*20)
# ---------------

my_list = ["emp-1", "emp-2", "emp-3", "emp-4"]
print("my_list", my_list, end="\n\n")

for j in my_list:
    print("Value stored in variable 'j' is:", j)
    if j == "emp-2":
        print("We are ending for-loop manually using 'break' statement")
        break

print("#"*40, end="\n\n")
############################

print("manually send it for next iteration using 'continue' statement")
print("-"*20)
# ---------------

my_list = ["emp-1", "emp-2", "emp-3", "emp-2", "emp-4"]
print("my_list", my_list, end="\n\n")

for j in my_list:
    if j == "emp-2":
        print("Manually send it for next iteration using 'continue' statement")
        continue
    print("Value stored in variable 'j' is:", j)

print("#"*40, end="\n\n")
############################

print("for-loop: WITHOUT using for-else block")
print("-"*20)
# ---------------

my_list = ["emp-1", "emp-2", "emp-3", "emp-4"]
print("my_list", my_list, end="\n\n")

# Requirement: verify whether "emp-3" present or not
# print "Found" or "Not Found"
my_flag = 0
for i in my_list:
    if i == "emp-3":
        my_flag = 1
        print("FOUND")
        print("Ending for-loop using 'break' statement")
        break
if my_flag == 0:
    print("Not Found")

print("#"*40, end="\n\n")
############################

print("for-loop: USING for-else block")
print("-"*20)
# ---------------

my_list = ["emp-1", "emp-2", "emp-30", "emp-4"]
print("my_list", my_list, end="\n\n")

# Requirement: verify whether "emp-3" present or not
# print "Found" or "Not Found"
# my_flag = 0
for i in my_list:
    if i == "emp-3":
        # my_flag = 1
        print("FOUND")
        print("Ending for-loop using 'break' statement")
        break
else:
    print("Reached for-else block")
    print("Not Found")

# point-1: 'else'-block will execute after completing for-loop
# point-2: 'break' statement will comeout from both for-block and 'for-else-block' #IMPORTANT

print("#"*40, end="\n\n")
############################

