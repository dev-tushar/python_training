"""
Exceptions Handling
"""

# print("WITHOUT Handling Exceptions")
# print("-"*20)
# # ---------------
#
# a = 10
# b = 0
# result = a/b
# print(result)
#
# print("#"*40, end="\n\n")
# ############################

print("Handling Exceptions using try-except blocks")
print("-"*20)
# ---------------
try:
    pass
    # Put any code here
    # if any error in this try-block then program will not terminate
    # instead it will send to 'except' block
except:
    print("Entering this block means there is a error in try-block")
    print("Write logic to take care of the error occurred in try-blok")


print("#"*40, end="\n\n")
############################

print("Handling Exceptions using try-except blocks with Example")
print("-"*20)
# ---------------
try:
    a = 10
    b =0
    c = a/b
    print("Value of c is :", c)
except:
    print("Reached except-block")
    print("There is error in try-block")

print("#"*40, end="\n\n")
############################

# ---------------
# How exception handling works?
# ---------------
# - If we want to handle exceptions using try-except block then
#   we need to have exception-classes for those error
#
# - If we don't have exception-class for any error then that error
#   we can't handle using try-except block. So, even though code is
#   present in try-block, program will terminate abruptly because that
#   error is not having exception-class
#
# - Few exception-classes are present in builtins
#
# - default except block will be able to understand all builtins exception-class
#   so, default except block will be able to handle all exception present in builtins
#
# - Above block  (c = a/b) is throwing divide by zero error, for this error we have exception-class
#   in builtin called 'ZeroDivisionError'. That why we are able to handle exception in above block
#
# - When we are using any library, almost all libraries will provide exception-classes
#   for those error expected while using that library
#
# - If we want to handle any other type of exception for those we don't have exception-class
#   then we need to write own exception class to handle
#
# - Super class for all exception-class is 'Exception'. Other-way, all exception
#   classes are inherited from 'Exception' class
#
# - We can specify class name in 'except' block
############################

print("Handling Exceptions using try-except blocks with exception classes")
print("-"*20)
# ---------------
try:
    L = ["Java", "Python"]
    print(L[100]) # 10th value not present so it is index error
    a = 10
    b =0
    c = a/b
    print("Value of c is :", c)
except ZeroDivisionError: # 1-way to specify class name
    print("This is ZDE except block")
except NameError as ne: # 2-way to specify class name where we are storing error message
    print("This is NameError block and captured error message is:", ne)
except Exception as e:
    print("This is default exception block which receives all other error. Current error message is:", e)

print("#"*40, end="\n\n")
############################

print("Total 4 block we can use in exceptions handling")
print("1) try-block 2) except-block 3) else-block 4) finally-block")
print("-"*20)
# ---------------

try:
    print("Writing to file")
    my_file_handle = open(file=r"D:\some\wrong\path.txt", mode="w")
    print("File opened successfully")
except Exception as e:
    print("Reached except-block")
    print("In this except block, we are handling file open error like filenotfound, permission error etc")
else:
    print("Reched else-block")
    print("If file open success, then we want to write data")
    my_file_handle.write("Hi")
    my_file_handle.write("Hello")
    print("All write completed")
finally:
    print("Reached finally-block")
    print("Irrespective of all the block success or failure, finally-block will always execute")
    print("In this example, whether all the blocks are success/failed, we want safely close the file handle")
    try:
        my_file_handle.close()
        print("File closed successfully")
    except Exception as e:
        print("Not able to close file handle because : ", e)

print("#"*40, end="\n\n")
############################

# ---------------
# how try-except-else-finally block works?
# ---------------
# About else-block
# - if try-block success then else-block will execute and 'except-block' will be skipped
# - if try-block fails then except-block will execute and 'else-block' will be skipped
#
# About finally-block
# - if error or no-error in any of the blocks like try/except/else then finally-block will always execute
############################


print("Example of using exception class from any library")
print("-" * 20)
# ---------------
import json

try:
    a = 10
    b = 0
    c = a / b
    print("Value of c is :", c)
except ZeroDivisionError:  # 1-way to specify class name
    print("This is ZDE except block")
except json.decoder.JSONDecodeError:
    print("This is JSONDecodeError block")

print("#" * 40, end="\n\n")
############################

print("User defined exception class example-1")
print("-"*20)
# ---------------
# Mandatory step to create use defined exception class is
# our class should be subclass of 'Exception' class
# OR
# if some classes are already subclass of 'Exception' class
#   then we can extend that class and create our own exception-class
#   example, all builtin exception classes are already subclass of
#   'Exception' class so we can ALSO extend those classes to create exception-class


class MyError(Exception):
    pass

# - MyError class is empty class but valid exception-class
# - valid exception-class means, we can use this class in try-except block to handle
#   exception
# - To MANUALLY throw any exception, including builtin-exception, we need to
#   use raise

try:
    x = 10
    if x == 10:
        raise MyError
    if x < 10:
        raise MyError
    if x > 10:
        raise MyError
except MyError:
    print("This is MyError block")

print("#"*40, end="\n\n")
############################

print("User defined exception class example-2")
print("-"*20)
# ---------------

# Requirement:
# 1- pass some message and error code while throwing exception
# 2- Write method for debug
# 3- write help method

class MyError(Exception):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code

    def how_to_debug(self):
        return "This is debug"

    def help(self):
        return "This is help"


try:
    x = 10
    if x == 10:
        raise MyError("Here value is 10 so MyError", 101)
    if x < 10:
        raise MyError("Here value is lt 10 so MyError", 102)
    if x > 10:
        raise MyError("Here value is gt 10 so MyError", 103)
except MyError as me:
    print("This is MyError block")
    print("Error message:", me.message)
    print("Error code:", me.error_code)
    print("Debug:", me.how_to_debug())
    print("Help message:", me.help())

print("#"*40, end="\n\n")
############################