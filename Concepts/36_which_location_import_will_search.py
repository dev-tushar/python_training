"""
In this section, 2 things
1. List of directories where import-statement will check for specified library
2. How to add new location where we have libraries
"""

print("1. List of directories where import-statement will check for specified library")
print("-"*20)
# ---------------

import sys
print(sys.path) # by default, import will refer this list of directories

print("#"*40, end="\n\n")
############################

print("2. How to add new location where we have libraries")
print("-"*20)
# ---------------

import sys
new_location_1 = r"D:\mylib1"
sys.path.append(new_location_1)
new_location_2 = r"D:\mylib2"
sys.path.append(new_location_2)
print(sys.path)

# NOTE: 1st we need to add new location to sys.path then write import-statement

print("#"*40, end="\n\n")
############################