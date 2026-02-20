"""
Get data from sample_data.txt

then

extract
IP
DATE
URL

then
make dictionary called my_dictionary

then dictionary to my_report_2.json

Expected content in my_dictionary:
{
    0 : ('123.123.123.123', '26/Apr/2000', 'http://www.jafsoft.com/asctortf/'),
    1 : ('123.123.123.123', '26/Apr/2000', 'http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF'),
    2 : ('123.123.123.123', '26/Apr/2000', 'http://www.jafsoft.com/asctortf/'),
    3 : ('123.123.123.123', '26/Apr/2000', 'http://www.jafsoft.com/asctortf/'),
    4 : ('123.123.123.123', '26/Apr/2000', 'http://www.jafsoft.com/asctortf/'),
    5 : ('123.123.123.123', '26/Apr/2000', 'http://www.jafsoft.com/asctortf/')
}
"""

print("Get data from sample_data.txt")
print("-"*20)
# ---------------

# Step-1: Connect to file
# ---------------
my_file_handle = open(file="sample_data.txt", mode="r")

# Step-2: Read and write text file
# ---------------
file_content_list = my_file_handle.readlines()

# Step-3: Disconnect from file
# ---------------
my_file_handle.close()

print(file_content_list)

print("#"*40, end="\n\n")
############################

print("Extract information and print")
print("-"*20)
# ---------------

for each_line in file_content_list:
    if each_line.startswith("123"):
        sp = each_line.split(" ")
        # print("sp:", sp)

        # IP
        ip =sp[0]

        # DATE
        raw_date = sp[3] # '[26/Apr/2000:00:23:48'
        start_index = 1
        end_index = raw_date.find(":")
        dt = raw_date[start_index:end_index]

        # URL
        raw_url = sp[10] # '"http://www.jafsoft.com/asctortf/"'
        url = raw_url[1 : -1]

        print(ip, dt, url)


print("#"*40, end="\n\n")
############################

# ---------------
# Expected Dictionary
# ---------------
# >>> my_dictionary = {}
# >>> each_line_tuple = ('ip', 'dt', 'url')
# >>> my_dictionary[0] = each_line_tuple
# >>> my_dictionary
# {0: ('ip', 'dt', 'url')}
# >>> each_line_tuple = ('ip', 'dt', 'url')
# >>> my_dictionary[1] = each_line_tuple
# >>> my_dictionary
# {0: ('ip', 'dt', 'url'), 1: ('ip', 'dt', 'url')}
# >>>
############################

print("Extract information and make dictionary")
print("-"*20)
# ---------------

my_dictionary = {}
key = 0
for each_line in file_content_list:
    if each_line.startswith("123"):
        sp = each_line.split(" ")
        # print("sp:", sp)

        # IP
        ip =sp[0]

        # DATE
        raw_date = sp[3] # '[26/Apr/2000:00:23:48'
        start_index = 1
        end_index = raw_date.find(":")
        dt = raw_date[start_index:end_index]

        # URL
        raw_url = sp[10] # '"http://www.jafsoft.com/asctortf/"'
        url = raw_url[1 : -1]

        each_line_tuple = (ip, dt, url)
        my_dictionary[key] = each_line_tuple
        key += 1


print(my_dictionary)

print("#"*40, end="\n\n")
############################

print("Write to 'my_report_2.json' :")
print("-"*20)
# ---------------

my_file_handle = open(file="my_report_2.json", mode="w")

import json
json.dump(my_dictionary, my_file_handle) # dump() is write method

my_file_handle.close()

print("Created my_report_2.json, Please check your file")

print("#"*40, end="\n\n")
############################

print("Read from 'my_report_2.json' :")
print("-"*20)
# ---------------

my_file_handle = open(file="my_report_2.json", mode="r")

import json
json_file_content = json.load(my_file_handle) # load() is read method

my_file_handle.close()

print("json_file_content:", json_file_content, end="\n\n")

print("type of json_file_content:", type(json_file_content), end="\n\n")

print("#"*40, end="\n\n")
############################