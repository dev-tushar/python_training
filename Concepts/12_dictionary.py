"""
Dictionary: We already have option to store multiple values like list of employee names.
        - We can store DUPLICATE values
        - MANUALLY We-can/we-have-to provide index to each value. KEY/VALUE pair
"""
print("Dictionary PART-1")
print("How to store values")
print("-"*20)
# ---------------
# Key can be number, string, tuple
# Value can be any type of value
my_dictionary = {
    "duration": 10,
     "course": "python",
     "mode": ["online", "offline"],
     "trainer": {"fname": "abc", "lname": "xyz"}
     }
print(my_dictionary)

print("#"*40, end="\n\n")
############################

print("Dictionary PART-2")
print("Accessing each value")
print("-"*20)
# ---------------

my_dictionary = {
    "duration": 10,
     "course": "python",
     "mode": ["online", "offline"],
     "trainer": {"fname": "abc", "lname": "xyz"}
     }
print("my_dictionary:", my_dictionary, end="\n\n")

print("duration:", my_dictionary["duration"])
print("course:", my_dictionary["course"])
print("mode:", my_dictionary["mode"])
print("trainer:", my_dictionary["trainer"])

print("#"*40, end="\n\n")
############################


print("Dictionary PART-3")
print("list of methods present in 'dict' class")
print("-"*20)
# ---------------

print(dir(my_dictionary))
# OR
print(dir(dict))

print("#"*40, end="\n\n")
############################

print("Dictionary PART-4")
print("ADD/REMOVE/UPDATE")
print("-"*20)
# ---------------

my_dictionary = {
    "duration": 10,
     "course": "python",
     "mode": ["online", "offline"],
     "trainer": {"fname": "abc", "lname": "xyz"}
     }
print("my_dictionary:", my_dictionary, end="\n\n")

# ADD/UPDATE: Procedure is same for both add/update, if key found then update else add new
my_dictionary["location"] = "India" # Here, key "location" not found so, it will add
print("my_dictionary after adding 'location':", my_dictionary, end="\n\n")

# Delete (ONLY POP is there, no REMOVE. In POP we give key of the entry to be deleted)
my_dictionary.pop("duration")
print("my_dictionary after removing 'duration':", my_dictionary, end="\n\n")

print("#"*40, end="\n\n")
############################