"""
Generator: It is a function. We can write function which can return one value at a time during iteration.
"""

print("WITHOUT using generator function")
print("-"*20)
# ---------------

# Requirement: print each squared value using for-loop

def my_square_function(my_list):
    squared_list = []
    for i in my_list:
        squared_list.append(i*i)
    return squared_list

L = [10, 20, 30, 40, 50]

# Requirement: print each squared value using for-loop. one by one

received_squared_list = my_square_function(L)
print("received_squared_list:", received_squared_list, end="\n\n")

for i in received_squared_list:
    print("Each squared value is :", i)

print("#"*40, end="\n\n")
############################

print("USING generator function")
print("-"*20)
# ---------------

# Requirement: print each squared value using for-loop

def my_square_generator_function(my_list):
    for i in my_list:
        yield i * i     #returns required value, then pauses in the same state

L = [10, 20, 30, 40, 50]

# Requirement: print each squared value using for-loop. one by one

received_squared_generator_object = my_square_generator_function(L)
print("received_squared_generator_object:", received_squared_generator_object, end="\n\n")

for i in received_squared_generator_object:
    print("Each squared value is :", i)

print("#"*40, end="\n\n")
############################