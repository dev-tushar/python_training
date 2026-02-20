"""
While-loop: Execute loop till the given condition is True.
"""

print("While-loop example")
print("-"*20)
# ---------------

x = 0
while x < 10:
    print("Value of x is:", x)
    x += 1

print("#"*40, end="\n\n")
############################

print("manually end for-loop using 'break' statement")
print("-"*20)
# ---------------

my_list = ["emp-1", "emp-2", "emp-3", "emp-4"]
print("my_list", my_list, end="\n\n")

index_no = 0
while index_no < len(my_list):
    j = my_list[index_no]
    index_no += 1
    print("Value stored in variable 'j' is:", j)
    if j == "emp-2":
        print("We are ending for-loop manually using 'break' statement")
        break

# for j in my_list:
#     print("Value stored in variable 'j' is:", j)
#     if j == "emp-2":
#         print("We are ending for-loop manually using 'break' statement")
#         break

print("#"*40, end="\n\n")
############################

print("manually send it for next iteration using 'continue' statement")
print("-"*20)
# ---------------

my_list = ["emp-1", "emp-2", "emp-3", "emp-2", "emp-4"]
print("my_list", my_list, end="\n\n")

index_no = 0
while index_no < len(my_list):
    j = my_list[index_no]
    index_no += 1
    if j == "emp-2":
        print("Manually send it for next iteration using 'continue' statement")
        continue
    print("Value stored in variable 'j' is:", j)


# for j in my_list:
#     if j == "emp-2":
#         print("Manually send it for next iteration using 'continue' statement")
#         continue
#     print("Value stored in variable 'j' is:", j)

print("#"*40, end="\n\n")
############################

print("while-loop: USING while-else block")
print("-"*20)
# ---------------

my_list = ["emp-1", "emp-2", "emp-30", "emp-4"]
print("my_list", my_list, end="\n\n")

# Requirement: verify whether "emp-3" present or not
# print "Found" or "Not Found"
index_no = 0
while index_no < len(my_list):
    i = my_list[index_no]
    index_no += 1
    if i == "emp-3":
        # my_flag = 1
        print("FOUND")
        print("Ending while-loop using 'break' statement")
        break
else:
    print("Reached while-else block")
    print("Not Found")


# # my_flag = 0
# for i in my_list:
#     if i == "emp-3":
#         # my_flag = 1
#         print("FOUND")
#         print("Ending for-loop using 'break' statement")
#         break
# else:
#     print("Reached for-else block")
#     print("Not Found")

# point-1: 'else'-block will execute after completing for-loop
# point-2: 'break' statement will comeout from both for-block and 'for-else-block'

print("#"*40, end="\n\n")
############################