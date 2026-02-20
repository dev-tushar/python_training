"""
Write below functions

# ------------------
Function-1: Write function named 'extract_data_function' which takes one argument
called 'in_file_path'. Function should read in_file then extract data from it then return extracted
data in dictionary.

# Test Function-1 like
received_data = extract_data_function("sample_data.txt")
print(received_data) # This should print dictionary
###################

# ------------------
Function-2: Write function named 'write_to_text_file_function' which takes 2 arguments
argument 1 is 'data' and argument 2 is 'out_file_name'. This function should write
data into output text file

# Test Function-2 like
write_to_text_file_function(received_data, "out_file.txt")
###################

# ------------------
Function-3: Write function named 'write_to_json_file_function' which takes 2 arguments
argument 1 is 'data' and argument 2 is 'out_file_name'. This function should write
data into output json file

# Test Function-3 like
write_to_json_file_function(received_data, "out_file.json")
###################
"""

"""
Write below functions

# ------------------
Function-1: Write function named 'extract_data_function' which takes one argument
called 'in_file_path'. Function should read in_file then extract data from it then return extracted
data in dictionary.

# Test Function-1 like
received_data = extract_data_function("sample_data.txt")
print(received_data) # This should print dictionary
###################

# ------------------
Function-2: Write function named 'write_to_text_file_function' which takes 2 arguments
argument 1 is 'data' and argument 2 is 'out_file_name'. This function should write
data into output text file

# Test Function-2 like
write_to_text_file_function(received_data, "out_file.txt")
###################

# ------------------
Function-3: Write function named 'write_to_json_file_function' which takes 2 arguments
argument 1 is 'data' and argument 2 is 'out_file_name'. This function should write
data into output json file

# Test Function-3 like
write_to_json_file_function(received_data, "out_file.json")
###################
"""

print("Writing 'extract_data_function' function")
print("-"*20)
# ---------------

def extract_data_function(input_data_file_path):
    """
    This function will take input_data_file_path,
    then
    it will read input_data_file content
    then
    it will extract data from input_data_file
    then
    it will return extracted data in dictionary
    :param input_data_file_path:
    :return my_dictionary:
    """
    # Get data from input file
    my_file_handle = open(file=input_data_file_path, mode="r")
    input_file_content = my_file_handle.readlines()
    my_file_handle.close()

    # Extract data and return in dictionary
    my_dictionary = {}
    key = 0
    for each_line in input_file_content:
        if each_line.startswith("123"):
            sp = each_line.split(" ")
            # print("sp:", sp)

            # IP
            ip = sp[0]

            # DATE
            raw_date = sp[3]  # '[26/Apr/2000:00:23:48'
            start_index = 1
            end_index = raw_date.find(":")
            dt = raw_date[start_index:end_index]

            # URL
            raw_url = sp[10]  # '"http://www.jafsoft.com/asctortf/"'
            url = raw_url[1: -1]

            each_line_tuple = (ip, dt, url)
            my_dictionary[key] = each_line_tuple
            key += 1
    return my_dictionary

print("#"*40, end="\n\n")
############################

print("Testing extract_data_function")
print("-"*20)
# ---------------

received_data = extract_data_function("sample_data.txt")
print(received_data)

print("#"*40, end="\n\n")
############################

print("Writing 'write_to_text_file_function' :")
print("-"*20)
# ---------------

def write_to_text_file_function(data, out_file_path):
    """
    This function will take 2 arguments
    argument 1 is 'data' and argument 2 is 'out_file_path'.
    then
    This function will write data into output text file
    :param data:
    :param out_file_path:
    :return None:
    """
    # >>> # Our Plan
    # >>> data = {0:('ip', 'dt', 'url'), 1:('ip', 'dt', 'url'),2:('ip', 'dt', 'url'),}
    # >>> data.values()
    # dict_values([('ip', 'dt', 'url'), ('ip', 'dt', 'url'), ('ip', 'dt', 'url')])
    # >>>
    my_out_file_handle = open(file=out_file_path, mode="w")
    print("IP", "DATE", "URL", sep="\t", file=my_out_file_handle)
    for each_tuple in data.values():
        print(each_tuple[0], each_tuple[1], each_tuple[2], sep="\t", file=my_out_file_handle)
    my_out_file_handle.close()

print("#"*40, end="\n\n")
############################

print("Testing 'write_to_text_file_function':")
print("-"*20)
# ---------------

write_to_text_file_function(received_data, "my_report_5.txt")
print("Created 'my_report_5.txt' file")

print("#"*40, end="\n\n")
############################

print("Writing 'write_to_json_file_function':")
print("-"*20)
# ---------------

def write_to_json_file_function(data, out_file_path):
    """
    This function will take 2 arguments
    argument 1 is 'data' and argument 2 is 'out_file_path'.
    then
    This function will write data into output json file
    :param data:
    :param out_file_path:
    :return None:
    """
    my_out_file_handle = open(file=out_file_path, mode="w")
    import json
    json.dump(data, my_out_file_handle)
    my_out_file_handle.close()

print("#"*40, end="\n\n")
############################

print("Testing write_to_json_file_function:")
print("-"*20)
# ---------------

write_to_json_file_function(received_data, "my_report_6.json")
print("Created 'my_report_6.json' file")

print("#"*40, end="\n\n")
############################