"""
Program on pandas
"""

"""
Problem Statement:

Get data from below sources

my_report_1.txt
my_report_2.json
mydb.db
web_scraping_report.json

then produce single report in below files

final_report.csv
final_report.xlsx
final_report.json
final_report.html
final_report.xml
"""


print("Get data from my_report_1.txt")
print("-"*20)
# ---------------

import pandas as pd
my_txt_report_df = pd.read_csv("my_report_1.txt", sep="\t") # default sep=","
print(my_txt_report_df)

my_txt_report_df.to_csv("tempcsv.csv") #To check how the data looks at present in a csv

print("#"*40, end="\n\n")
############################

print("Get data from my_report_2.json: PART-1")
print("Reading json file")
print("-"*20)
# ---------------

import pandas as pd

my_json_report_df = pd.read_json("my_report_2.json")
print(my_json_report_df)

print("#"*40, end="\n\n")
############################

print("Get data from my_report_2.json: PART-2")
print("Rotate dataframe")
print("-"*20)
# ---------------

my_json_report_df = my_json_report_df.transpose()
print(my_json_report_df)

print("#"*40, end="\n\n")
############################

print("Get data from my_report_2.json: PART-3")
print("Current column names")
print("-"*20)
# ---------------

column_names = my_json_report_df.columns
print(column_names)

print("#"*40, end="\n\n")
############################

print("Get data from my_report_2.json: PART-4")
print("Rename the columns")
print("-"*20)
# ---------------

my_json_report_df.columns = ["IP", "DATE", "URL"]
print(my_json_report_df)

print("#"*40, end="\n\n")
############################

print("Get data from my_report_2.json: PART-5")
print("Current column names after rename")
print("-"*20)
# ---------------

column_names = my_json_report_df.columns
print(column_names)

print("#"*40, end="\n\n")
############################

print("Get data from mydb: PART-1")
print("-"*20)
# ---------------

import sqlite3
my_db_connection = sqlite3.connect("mydb.db")

# 2-way to read/write to database is, using pandas
# So, using pandas also we can communicate with database
import pandas as pd
my_db_data_df = pd.read_sql("SELECT * FROM mytable", my_db_connection)
print(my_db_data_df)

print("#"*40, end="\n\n")
############################


print("Get data from mydb: PART-2")
print("Rename column names to capital letters")
print("-"*20)
# ---------------

my_db_data_df.columns = ["IP", "DATE", "URL"]
print(my_db_data_df)

print("#"*40, end="\n\n")
############################

#
# print("Get data from web_scraping_report.json: PART-1")
# print("-"*20)
# # ---------------
#
# import pandas as pd
# my_web_scraping_report_df = pd.read_json("web_scraping_report.json")
# print(my_web_scraping_report_df)
#
# print("#"*40, end="\n\n")
# ############################

# ---------------
# We can't read using above option, because json file content
# is not compatible with tabular format. So manually
# we read json file using json library and bring to tabular format
############################

# ---------------
# How we want web_scraping_report.json file content in xlsx?
# ---------------
# point-1:  expected columns:
#           title_tag_text	top_menu_items	all_paragraph_contents	All Urls	attribute name	attribute value
#
# point-2: We are planning to make dictionary where
#   keys will be column names and values we will bring into list format
#   then DataFrame([ [],  [], []], columns=my_dictionary.keys())
############################

print("Get data from web_scraping_report.json: PART-1")
print("Reading file")
print("-"*20)
# ---------------

my_web_scraping_report_file_handle = open(file="web_scraping_report.json", mode="r")

import json
my_web_scraping_data = json.load(my_web_scraping_report_file_handle) # reading

my_web_scraping_report_file_handle.close()

print(my_web_scraping_data)


print("#"*40, end="\n\n")
############################

print("Get data from web_scraping_report.json: PART-2")
print("put title tag text in list. currently it is string")
print("-"*20)
# ---------------

my_web_scraping_data["title_tag_text"] = [ my_web_scraping_data["title_tag_text"] ]
print(my_web_scraping_data)

print("#"*40, end="\n\n")
############################

print("Get data from web_scraping_report.json: PART-3")
print("1. Add new column: attribute_names  ")
print("2. Add new column: attribute_values  ")
print("3. remove  script_tag_attributes ")
print("-"*20)
# ---------------

# my_web_scraping_data = { 'script_tag_attributes': {'defer': '', 'file-types': 'bz2,chm,dmg,exe,gz,json,msi,msix,pdf,pkg,tgz,xz,zip', 'data-domain': 'python.org', 'src': 'https://analytics.python.org/js/script.file-downloads.outbound-links.js'},}

# 1.  Add new column/key: attribute_names
my_web_scraping_data["attribute_names"] = my_web_scraping_data["script_tag_attributes"].keys()

print("$$$$$",my_web_scraping_data["attribute_names"])
# convert to list
my_web_scraping_data["attribute_names"] = list(my_web_scraping_data["attribute_names"])

# 2. Add new column: attribute_values
my_web_scraping_data["attribute_values"] = my_web_scraping_data["script_tag_attributes"].values()
# convert to list
my_web_scraping_data["attribute_values"] = list(my_web_scraping_data["attribute_values"])

# 3. remove  script_tag_attributes
my_web_scraping_data.pop("script_tag_attributes")

print("Json after removing 'script tag attributes and "
      "storing its keys and values in "
      "new columns 'attribute name' and 'attribute values' ", end="\n\n")
print(my_web_scraping_data)

print("#"*40, end="\n\n")
############################

print("Get data from web_scraping_report.json: PART-4")
print("Create dataframe class object with web_scraping_data")
print("-"*20)
# ---------------

import pandas as pd
my_web_scraping_report_df = pd.DataFrame(data=my_web_scraping_data.values())
print(my_web_scraping_report_df)

print("#"*40, end="\n\n")
############################


print("Get data from web_scraping_report.json: PART-5")
print("Rotate dataframe")
print("-"*20)
# ---------------

my_web_scraping_report_df = my_web_scraping_report_df.transpose()
print(my_web_scraping_report_df)

print("#"*40, end="\n\n")
############################

print("Get data from web_scraping_report.json: PART-6")
print("Provide Column Names")
print("-"*20)
# ---------------

my_web_scraping_report_df.columns = my_web_scraping_data.keys()
print(my_web_scraping_report_df)

print("#"*40, end="\n\n")
############################

print("Get data from web_scraping_report.json: PART-7")
print("Empty cells")
print("-"*20)
# ---------------


print(my_web_scraping_report_df.isnull())

print("#"*40, end="\n\n")
############################

print("Get data from web_scraping_report.json: PART-8")
print("Total Empty cells")
print("-"*20)
# ---------------

print(my_web_scraping_report_df.isnull().sum())

print("#"*40, end="\n\n")
############################

print("Get data from web_scraping_report.json: PART-9")
print("Total Empty cells on entire data")
print("-"*20)
# ---------------

print(my_web_scraping_report_df.isnull().sum().sum())

print("#"*40, end="\n\n")
############################

print("Get data from web_scraping_report.json: PART-10")
print("Fill title column empty cells with 'new title'")
print("-"*20)
# ---------------

my_web_scraping_report_df["title_tag_text"] = my_web_scraping_report_df["title_tag_text"].fillna("New Title")
print(my_web_scraping_report_df)

print("#"*40, end="\n\n")
############################

print("Get data from web_scraping_report.json: PART-11")
print("On entire data, fill empty cells with 'new content'")
print("-"*20)
# ---------------

my_web_scraping_report_df = my_web_scraping_report_df.fillna("New Content")
print(my_web_scraping_report_df)

my_web_scraping_report_df.to_csv("tempcsv.csv")

print("#"*40, end="\n\n")
############################

# ---------------
# Plan for merging all 4 file contents
# ---------------

# Merge below 3 file contents: One below the other
# my_txt_report_df
# my_json_report_df
# my_db_data_df

# Merge vertically so that it will become new columns
# my_web_scraping_report_df
############################

print("Merge 3 file contents: One below the other: PART-1")
print("-"*20)
# ---------------

all_in_one_df = pd.concat([my_txt_report_df, my_json_report_df, my_db_data_df], axis=0)
# axis=0 : Merge vertically, one below the other
# axis=1 : Merge horizontally(columns next to each other), so it will become new columns
print(all_in_one_df)

print("#"*40, end="\n\n")
############################

print("Merge 3 file contents: One below the other: PART-2")
print("Reset index")
print("-"*20)
# ---------------

all_in_one_df = all_in_one_df.reset_index(drop=True) # drop=True: remove existing index column, if 'drop' not used
                                                    # then old index(row names) become a new column
print(all_in_one_df)

print("#"*40, end="\n\n")
############################

print("Merge vertically, so it will become new columns: PART-1")
print("-"*20)
# ---------------

# all_in_one_df
# my_web_scraping_report_df

all_in_one_df = pd.concat([all_in_one_df, my_web_scraping_report_df], axis=1)
print(all_in_one_df)

print("#"*40, end="\n\n")
############################

print("Merge vertically, so it will become new columns: PART-2")
print("Fill null values with 'final value'")
print("-"*20)
# ---------------
all_in_one_df = all_in_one_df.fillna("final value")
print(all_in_one_df)

print("#"*40, end="\n\n")
############################

print("Write to final report")
print("-"*20)
# ---------------

all_in_one_df.to_csv("final_report.csv", index=False)
all_in_one_df.to_excel("final_report.xlsx", index=False)
all_in_one_df.to_json("final_report_1.json")
tmp_df = all_in_one_df.transpose()
tmp_df.to_json("final_report_2.json")
all_in_one_df.to_xml("final_report.xml")
all_in_one_df.to_html("final_report.html")

print("""
Created below files, Please check
final_report.csv
final_report.xlsx
final_report_1.json
final_report_2.json
final_report.xml
final_report.html
""")

print("#"*40, end="\n\n")
############################

print("Send it database as well")
print("-"*20)
# ---------------

import sqlite3
my_db_connection = sqlite3.connect("mydb.db")

all_in_one_df.to_sql(name="final_report_table", con=my_db_connection, if_exists="replace")

my_db_connection.close()

print("Created 'final_report_table' in database. Please check")

print("#"*40, end="\n\n")
############################