"""
multithreading:
    - In python multithreading is not parallel.
   -  https://docs.python.org/3/library/threading.html
multiprocessing:
    - it is parallel execution
    - https://docs.python.org/3/library/multiprocessing.html
"""

"""
If In python multithreading is not parallel.
then why they supported multithreading?
-- Still using multithreading in python is useful.
-- when we are using multithreading in python,
    if one thread is waiting some resource then
    that time interpreter will execute another thread
    So, this is the advantage of using multithreading in python

if we want complete parallel then
we can use multiprocessing
"""

"""
Parallel execution using multithreading and multiprocessing
"""

"""
- When run any program, 1st it will create one 'process' then
    it will execute the 'process'.
- If the program is taking some time to execute then
    we can also check this 'process' in task-manager
"""

"""
To speedup the execution, we have 2 options

multithreading: 
    Divide single program into multiple pieces and run parallelly. each piece is called thread
    So, it is SINGLE PROCESS but multiple threads

multiprocessing: 
    Divide single program into multiple pieces and run each piece as one process.
    So, Here splitting SINGLE PROCESS into multiple process
"""

print("WITHOUT using multithreading")
print("-"*20)
# ---------------

import time

start = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("SQUARE:", i*i)

def my_cube_function(my_list):
    for i in my_list:
        print("CUBE:", i*i*i)

L = [10, 20, 30, 40, 50]
my_square_function(L)
my_cube_function(L)

end = time.time()
print("Total time:", end-start)

print("#"*40, end="\n\n")
############################


print("USING multithreading")
print("-"*20)
# ---------------

import time

start = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("SQUARE:", i*i)

def my_cube_function(my_list):
    for i in my_list:
        print("CUBE:", i*i*i)

from threading import Thread

L = [10, 20, 30, 40, 50]
my_thread_1 = Thread(target=my_square_function, args=(L,))
my_thread_2 = Thread(target=my_cube_function, args=(L,))

my_thread_1.start()
my_thread_2.start()
# start() will just start the thread and proceed to next line,
# start() will not wait for thread to complete

my_thread_1.join() # Wait here till my_thread_1 completes its execution
my_thread_2.join() # Wait here till my_thread_1 completes its execution

end = time.time()
print("Total time:", end-start)

print("#"*40, end="\n\n")
############################

print("WITH DELAY: WITHOUT using multithreading")
print("-"*20)
# ---------------

import time

start = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("SQUARE:", i*i)
        time.sleep(0.1)

def my_cube_function(my_list):
    for i in my_list:
        print("CUBE:", i*i*i)
        time.sleep(0.1)

L = [10, 20, 30, 40, 50]
my_square_function(L)
my_cube_function(L)

end = time.time()
print("Total time:", end-start)

print("#"*40, end="\n\n")
############################


print("WITH DELAY: USING multithreading")
print("-"*20)
# ---------------

import time

start = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("SQUARE:", i*i)
        time.sleep(0.1)

def my_cube_function(my_list):
    for i in my_list:
        print("CUBE:", i*i*i)
        time.sleep(0.1)

from threading import Thread

L = [10, 20, 30, 40, 50]
my_thread_1 = Thread(target=my_square_function, args=(L,))
my_thread_2 = Thread(target=my_cube_function, args=(L,))

my_thread_1.start()
my_thread_2.start()
# start() will just start the thread and proceed to next line,
# start() will not wait for thread to complete

my_thread_1.join() # Wait here till my_thread_1 completes its execution
my_thread_2.join() # Wait here till my_thread_1 completes its execution

end = time.time()
print("Total time:", end-start)

print("#"*40, end="\n\n")
############################