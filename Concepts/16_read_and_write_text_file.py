"""
Read and write text file with any extension like .txt, .log, .mylog etc
"""

"""
We need to follow 3 steps
Step-1: Connect to file
Step-2: Read and write text file
Step-3: Disconnect from file
"""

"""
We have functions for all 3 steps
Step-1: Connect to file
    - open() function
Step-2: Read and write text file
    - For WRITING: 1) write() 2) writelines() 3) print() function
    - For Reading: 1) read() 2) readlines() 3) readline()
Step-3: Disconnect from file
    - close() function
"""

# -----------
# Modes
##########
# mode 'w':
#   -- It will create new file
#   -- It will erase existing file content and make it empty file
#   -- It is write only, we can't read
#
# mode 'r':
#   -- It will NOT create new file
#   -- It is read only, we can't write
#
# mode 'a':
#   -- It will create new file, only if file not present
#   -- It will append to existing, we can't read
#
# POINT-1: If we add + to any mode, it enables read/write both
#       like w+, r+, a+
# POINT-2: If we add 'b' then it is read binary file
#      like wb, rb, ab
####################

print("All write operations")
print("-"*20)
# ---------------

# Step-1: Connect to file
# ---------------
my_file_handle = open(file="myfile.txt", mode="w")

# Step-2: Read and write text file
# ---------------

# Our Data
x = 10
y = "Python"

# 1) write() : it will take single value in STRING of any size (ONLY STRINGS(TEXT) can be stored
#       inside a file, not integer etc.)
my_file_handle.write(str(x)+"\n")
my_file_handle.write(y+"\n")

# 2) writelines(): It will take multiple values in any collection like list/tuple etc
my_list = [str(x)+"\n", y+"\n"]
my_file_handle.writelines(my_list)

# 3) print() function
print(x, y, 20, "Java", sep="\n", file=my_file_handle)
# - Total 3 parameters we can pass to print() function 1) sep 2) end 3) file
# - file=my_file_handle : Now print to write to file, not to console
# - no need of converting x and 20 to string, print will take care of this

# Step-3: Disconnect from file
# ---------------
my_file_handle.close()

print("Created 'myfile.txt' file, Please check'")

print("#"*40, end="\n\n")
############################

# ---------------
# How to provide file path?
# ---------------
# OPTION-1: refers current directory
# file="myfile.txt"
#
# OPTION-2: absolute path
# file = r"C:\python_training\concepts\myfile.txt"
#
# OPTION-3: Relative path
# file ="../programs/myfile.txt"
############################

print("Read 'myfile.txt' file using 1) read() method")
print("-"*20)
# ---------------

# Step-1: Connect to file
# ---------------
my_file_handle = open(file="myfile.txt", mode="r")

# Step-2: Read and write text file
# ---------------
file_content = my_file_handle.read()
# read() method will read entire file content and returns entire file content in string
print("file_content:", file_content, end="\n\n")
print("file_content in raw format:", repr(file_content), end="\n\n")

# Step-3: Disconnect from file
# ---------------
my_file_handle.close()

print("#"*40, end="\n\n")
############################

print("Read 'myfile.txt' file using 2) readlines() method")
print("-"*20)
# ---------------

# Step-1: Connect to file
# ---------------
my_file_handle = open(file="myfile.txt", mode="r")

# Step-2: Read and write text file
# ---------------
file_content = my_file_handle.readlines()
# readlines() method will read entire file content and returns entire file content in list
print("file_content:", file_content, end="\n\n")

# Step-3: Disconnect from file
# ---------------
my_file_handle.close()

print("#"*40, end="\n\n")
############################

print("Read 'myfile.txt' file using 3) readline() method")
print("-"*20)
# ---------------

# Step-1: Connect to file
# ---------------
my_file_handle = open(file="myfile.txt", mode="r")

# Step-2: Read and write text file
# ---------------
file_content = my_file_handle.readline()
# readline() method will read one and returns one line
print("1st line", file_content, end="\n\n")

file_content = my_file_handle.readline()
# readline() method will read one and returns one line
print("2nd line", file_content, end="\n\n")

file_content = my_file_handle.readline()
# readline() method will read one and returns one line
print("3rd line", file_content, end="\n\n")

# Step-3: Disconnect from file
# ---------------
my_file_handle.close()

print("#"*40, end="\n\n")
############################

print("Read 'myfile.txt' file using 4) read line by line using for-loop")
print("-"*20)
# ---------------

# Step-1: Connect to file
# ---------------
my_file_handle = open(file="myfile.txt", mode="r")

# Step-2: Read and write text file
# ---------------
for each_line in my_file_handle:
    print("Each_line:", each_line)

# Step-3: Disconnect from file
# ---------------
my_file_handle.close()

print("#"*40, end="\n\n")
############################