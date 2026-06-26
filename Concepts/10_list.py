"""
 list: We already have option to store multiple values like list of employee names.
        - We can store DUPLICATE values
        - Automatically index number will be assigned to each and every values
"""

print("list PART-1")
print("How to store multiple values like list of employee names:")
print("-"*20)
# ---------------

my_list = [10, 12.5, "emp-1", "emp-2", ("comp-1", "comp-2")]
print(my_list)
# Internally it will create object of builtin class 'list' and store multiple values inside that object

print("#"*40, end="\n\n")
############################

print("list PART-2")
print("Indexing is similar to strings. so all 4 types will work here as well")
print("-"*20)
# ---------------

my_list = [10, 12.5, "emp-1", "emp-2", ("comp-1", "comp-2")]
print(my_list)
# Internally it will create object of builtin class 'list' and store multiple values inside that object

print("1st Value:", my_list[0])
print("2nd Value:", my_list[1])
print("3rd Value:", my_list[2])
print("4th Value:", my_list[3])
print("5th Value:", my_list[4])

print("#"*40, end="\n\n")
############################


print("list PART-3")
print("Methods present inside list class")
print("-"*20)
# ---------------

my_list = [10, 12.5, "emp-1", "emp-2", ("comp-1", "comp-2")]
print(my_list)
# Internally it will create object of builtin class 'list' and store multiple values inside that object

print(dir(my_list))

print("#"*40, end="\n\n")
############################

print("list PART-4")
print("Learning 'count' and 'index' methods")
print("-"*20)
# ---------------
#
my_list = [10, 12.5, "emp-1", "emp-2", "emp-20","emp-20","emp-2",("comp-1", "comp-2")]
print(my_list)
# Internally it will create object of builtin class 'list' and store multiple values inside that object

count_of_emp2 = my_list.count("emp-2")

print("count_of_emp2:", count_of_emp2) # 4

index_of_emp2 = my_list.index("emp-2") # returns 1st occurance index
print("index_of_emp2:", index_of_emp2)

index_of_second_emp2 = my_list.index("emp-2", 4) # Start looking from index 4, instead if index-0
print("index_of_second_emp2:", index_of_second_emp2)

print("#"*40, end="\n\n")
############################

print("list PART-5")
print("ADD/UPDATE/DELETE methods")
print("-"*20)
# ---------------
#
my_list = ["emp-1", "emp-2", "emp-3", "emp-4", "emp-5", "emp-6"]
print(my_list)
# Internally it will create object of builtin class 'list' and store multiple values inside that object

# Add
my_list.append("emp-7")
print("my_list after appending emp-7:", my_list)
it=0
while it< len(my_list):
 print(f"my_list[{it}] is: ",my_list[it])
 it+=1

# Update
my_list[2] = "emp-300"
print("my_list after updating 3rd value with emp-300:", my_list)

# Delete
my_list.pop(3) #removing using index
my_list.remove("emp-300") #removing using value
print("my_list after deleting emp-4 at index-3:", my_list)

print("#"*40, end="\n\n")
############################