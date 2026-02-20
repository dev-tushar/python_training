"""
Get data from sample_data.txt

then extract
IP
DATE
URL
using regular expression

then
send extracted data to databases
"""

"""
How to communicate with any databases using python?
- We have a libraries for each database

python-program  <--Communicate using library--> any databases(SQL/NoSql)

Example:
python-program  <--Communicate using library oracledb--> Oracle database
python-program  <--Communicate using library mysql-connector-python--> MySQL database
python-program  <--Communicate using library sqlite3--> SQLite database
"""

"""
We need one database.
- We can use SQLite database
"""

"""
How to install/create and communicate with sqlite database?
2 options we have
Option-1: Using sqlite database software
Option-2: WITHOUT Using sqlite database software, USING python
    library 'sqlite3', we can create and communicate with sqlite database 
"""

"""
About SQLite database
- SQLite database is lightweight database
- SQLite database is not running any database server
- SQLite database is small database
- SQLite database is just one file
Since it is JUST one file, python library 'sqlite3' can create this database
BUT other databases, we need to install somewhere/somecloud/in-local
then we need to provide credentials to library. So, python library will
not create other databases which is running database server 
"""

print("Create/connect to database 'mydb.db' :")
print("-"*20)
# ---------------

import sqlite3

print("Create/connect to database 'mydb.db' :")
my_db_connection = sqlite3.connect("mydb.db")
print("Done\n")

print("Create cursor object")
my_db_cursor = my_db_connection.cursor()
print("Done\n")

print("Create table if not exists")
my_sql_create_table_query = """
create table if not exists mytable
(
ip varchar(100),
dt varchar(100),
url varchar(100)
)
"""
my_db_cursor.execute(my_sql_create_table_query)
print("Done\n")


print("#"*40, end="\n\n")
############################

print("Get data from sample_data.txt")
print("-"*20)
# ---------------

my_file_handle = open(file="sample_data.txt", mode="r")
file_content = my_file_handle.readlines()
my_file_handle.close()

print(file_content)

print("#"*40, end="\n\n")
############################

print("Extract IP, DATE, URL and print")
print("-"*20)
# ---------------

import re
for each_line in file_content:
    match_result = re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*(\d{2}/[A-Za-z]{3}/\d{4}).*(http[s]?://[a-z./A-Z_]+)', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        url = match_result.group(3)
        print(ip, dt, url)

print("#"*40, end="\n\n")
############################

print("Extract IP, DATE, URL and insert into mytable")
print("-"*20)
# ---------------

import re
for each_line in file_content:
    match_result = re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*(\d{2}/[A-Za-z]{3}/\d{4}).*(http[s]?://[a-z./A-Z_]+)', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        url = match_result.group(3)
        my_sql_insert_query = f"insert into mytable values('{ip}','{dt}','{url}')"
        # f-> format, it will replace {var_name} with value
        print("my_sql_insert_query:", my_sql_insert_query)
        my_db_cursor.execute(my_sql_insert_query)
        print("One record inserted\n")

my_db_connection.commit()
print("All records inserted, Please check database\n")

print("#"*40, end="\n\n")
############################

print("Get data from database and print")
print("-"*20)
# ---------------

my_sql_select_query = "SELECT * FROM mytable"
my_db_cursor.execute(my_sql_select_query)
my_db_result = my_db_cursor.fetchall()
my_db_connection.close()

print(my_db_result)
print("\n Records are inserted into database as well. Please check database\n")
print("#"*40, end="\n\n")
############################