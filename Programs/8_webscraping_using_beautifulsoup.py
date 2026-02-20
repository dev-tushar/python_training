"""
Webscraping using beautifulsoup library
"""

"""
Requirement:
From the website "www.python.org"
1. Get 1st script tag attributes
2. Get title tag text
3. Get top menu items
4. Get all the paragraphs
5. Get all links
Finally put all information in json file
"""

print("Read and print website data")
print("-"*20)
# ---------------

import requests
response = requests.get("http://www.python.org")
website_data = response.text
print(website_data)

print("#"*40, end="\n\n")
############################

print("Create object of beautifulsoup class and store website_content inside that object")
print("-"*20)
# ---------------

from bs4 import BeautifulSoup
soup = BeautifulSoup(website_data, "html.parser")
print(soup)

print("#"*40, end="\n\n")
############################

print("Neat Display")
print("-"*20)
# ---------------

print(soup.prettify())

print("#"*40, end="\n\n")
############################

print("Entire website content in string")
print("-"*20)
# ---------------

print(soup.get_text())

print("#"*40, end="\n\n")
############################


print("Get 1st script tag on entire website content")
print("-"*20)
# ---------------

script_tag = soup.script
print(script_tag)

print("#"*40, end="\n\n")
############################

print("Get 1st script tag within head tag")
print("-"*20)
# ---------------

script_tag = soup.head.script
print(script_tag)

print("#"*40, end="\n\n")
############################

print("Script tag attributes")
print("-"*20)
# ---------------

script_tag = soup.head.script
script_tag_attributes = script_tag.attrs
print(script_tag_attributes)

print("#"*40, end="\n\n")
############################


print("Get title tag ")
print("-"*20)
# ---------------

title_tag = soup.title
# OR
title_tag = soup.head.title
print(title_tag)

print("#"*40, end="\n\n")
############################

print("Get title tag text ")
print("-"*20)
# ---------------

title_tag_text = soup.head.title.text
print(title_tag_text)

print("#"*40, end="\n\n")
############################

print("Get top menu items: PART-1")
print("-"*20)
# ---------------

part_1_html_data = soup.body.div.find(id="top")
print(part_1_html_data)

print("#"*40, end="\n\n")
############################

print("Get top menu items: PART-2")
print("-"*20)
# ---------------

part_2_html_data = part_1_html_data.nav.ul
print(part_2_html_data)

print("#"*40, end="\n\n")
############################

print("Get top menu items: PART-3")
print("-"*20)
# ---------------

part_3_html_data = part_2_html_data.find_all('li')
print(part_3_html_data)

print("#"*40, end="\n\n")
############################

print("Get top menu items: PART-4")
print("Accessing each li-tag ")
print("-"*20)
# ---------------

for each_li_tag in part_3_html_data:
    print("each_li_tag:", each_li_tag, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
############################

print("Get top menu items: PART-5")
print("Accessing a-tag or anchor-tag from each li-tag ")
print("-"*20)
# ---------------

for each_li_tag in part_3_html_data:
    print("each_a_tag:", each_li_tag.a, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
############################

print("Get top menu items: PART-6")
print("Accessing menu item from each a-tag ")
print("-"*20)
# ---------------

for each_li_tag in part_3_html_data:
    print("Menu Item:", each_li_tag.a.text, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
############################

print("Get top menu items: PART-7")
print("Keeping all menu items in list")
print("-"*20)
# ---------------

top_menu_items = []
for each_li_tag in part_3_html_data:
    top_menu_items.append(each_li_tag.a.text)

print(top_menu_items)

print("#"*40, end="\n\n")
############################

print("Get all the paragraphs: PART-1")
print("Get all paragraph tags")
print("-"*20)
# ---------------

all_paragraph_tags = soup.find_all('p')
print(all_paragraph_tags)

print("#"*40, end="\n\n")
############################


print("Get all the paragraphs: PART-2")
print("Get all paragraph content")
print("-"*20)
# ---------------

# This time we will use one liner, something like comprehension
# we can write expression inside list/tuple/dictionary/set

all_paragraph_contents = [each_p_tag.text       for each_p_tag in all_paragraph_tags]
print(all_paragraph_contents)

print("#"*40, end="\n\n")
############################

print("Get all links: PART-1")
print("Get all a-tag or anchor-tag")
print("-"*20)
# ---------------

all_anchor_tags = soup.find_all('a')
print(all_anchor_tags)

print("#"*40, end="\n\n")
############################

# ---------------
# Dictionary Example
# ---------------
# >>> D = {"course": "Python", "mode": "online"}
# >>> # 2 ways to access values
# >>> # 1-way
# >>> D["course"]
# 'Python'
# >>> D["location"] # Key not present so it will throw error
# Traceback (most recent call last):
#   File "<pyshell#4>", line 1, in <module>
#     D["location"] # Key not present so it will throw error
# KeyError: 'location'
# >>> # 2-way to access values
# >>> D.get("course")
# 'Python'
# >>> D.get("location") # If key not present then it will return None. It will Not throw Error
############################

print("Get all links: PART-2")
print("Get attribute 'href' from each tag")
print("-"*20)
# ---------------

all_urls = [each_a_tag.get('href')          for each_a_tag in all_anchor_tags]
print(all_urls)

print("#"*40, end="\n\n")
############################

print("Get all links: PART-3")
print("Get only urls starting with 'http'")
print("-"*20)
# ---------------

all_urls = [each_url   for each_url in all_urls    if each_url.startswith('http')]
print(all_urls)

# - 1st startswith for-loop
# - then check right-side condition
# - if condition-true then execute left-side statement
#       i.e, each_url which does nothing, simple add each_url to new list
# - if right-side condition is false then goto next iteration

print("#"*40, end="\n\n")
############################

print("Create dictionary with all extracted data")
print("-"*20)
# ---------------

my_dictionary = {
"script_tag_attributes": script_tag_attributes,
    "title_tag_text": title_tag_text,
    "top_menu_items": top_menu_items,
    "all_paragraph_contents": all_paragraph_contents,
    "all_urls": all_urls
}

print(my_dictionary)

print("#"*40, end="\n\n")
############################

print("Create web_scraping_report.json file")
print("-"*20)
# ---------------

my_json_file_handle = open(file="web_scraping_report.json", mode="w")

import json
json.dump(my_dictionary, my_json_file_handle)

my_json_file_handle.close()

print("Created web_scraping_report.json file. Please check the file name.")

print("#"*40, end="\n\n")
############################