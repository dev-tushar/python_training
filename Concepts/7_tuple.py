"""
 Tuple: We already have option to store multiple values like list of employee names.
        - We can store DUPLICATE values
        - Automatically index number will be assigned to each and every values
"""

print("Tuple PART-1")
print("How to store multiple values like list of employee names:")
print("-"*20)
# ---------------

my_tuple = (10, 12.5, "emp-1", "emp-2", ("comp-1", "comp-2"))
print(my_tuple)
# Internally it will create object of builtin class 'tuple' and store multiple values inside that object

print("#"*40, end="\n\n")
############################

print("Tuple PART-2")
print("Indexing is similar to strings. so all 4 types will work here as well")
print("-"*20)
# ---------------

my_tuple = (10, 12.5, "emp-1", "emp-2", ("comp-1", "comp-2"))
print(my_tuple)
# Internally it will create object of builtin class 'tuple' and store multiple values inside that object

print("1st Value:", my_tuple[0])
print("2nd Value:", my_tuple[1])
print("3rd Value:", my_tuple[2])
print("4th Value:", my_tuple[3])
print("5th Value:", my_tuple[4])

print("#"*40, end="\n\n")
############################


print("Tuple PART-3")
print("Methods present inside tuple class")
print("-"*20)
# ---------------

my_tuple = (10, 12.5, "emp-1", "emp-2", ("comp-1", "comp-2"))
print(my_tuple)
# Internally it will create object of builtin class 'tuple' and store multiple values inside that object

print(dir(my_tuple))

print("#"*40, end="\n\n")
############################

print("Tuple PART-4")
print("Learning 'count' and 'index' methods")
print("-"*20)
# ---------------

my_tuple = (10, 12.5, "emp-1", "emp-2", "emp-20","emp-20","emp-2",("comp-1", "comp-2"))
print(my_tuple)
# Internally it will create object of builtin class 'tuple' and store multiple values inside that object

count_of_emp2 = my_tuple.count("emp-2")
print("count_of_emp2:", count_of_emp2) # 2 (count returns number of occurrences)

index_of_emp2 = my_tuple.index("emp-2") # returns 1st occurance index
print("index_of_emp2:", index_of_emp2)

index_of_second_emp2 = my_tuple.index("emp-2", 4) # Start looking from index 4, instead of index-0
print("index_of_second_emp2:", index_of_second_emp2)

print("#"*40, end="\n\n")
############################x