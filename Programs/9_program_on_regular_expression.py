"""
Get data from sample_data.txt

then
extract
IP
DATE
URL
using regular expression
"""

print("Get data from sample_data.txt")
print("-"*20)
# ---------------

my_file_handle = open(file="sample_data.txt", mode="r")
file_content = my_file_handle.readlines()
my_file_handle.close()

print(file_content)

print("#"*40, end="\n\n")
############################

# ---------------
# Regular Expression PART-1
# ---------------
r"""
IDENTIFIERS
-----------
# Shortcuts:

\d -> to tell it is ONE digit. Any one digit between 0 to 9
\D -> to tell it is any ONE non-digit. any character except 0 to 9
\s -> to tell one space
\S -> to tell any character except space
\w -> to tell any ONE character in this group of characters [a-zA-Z_0-9]
\W -> to tell any ONE character EXCEPT characters present in this group [^a-zA-Z_0-9]
. -> to tell any ONE any character
\. -> to tell strictly DOT only. not any character
-----------
"""
############################

# ---------------
# Regular Expression PART-2
# ---------------
"""
# Custom Identifiers

[a-b] -> match only any ONE lower case letter
[0-5] -> match only any ONE digit between 0 to 5
[^0-5a-z] -> match only any character except 0 to 5 and all lower case letter
[a0x5] -> match any ONE character in this group. 
    - It can be 'a' or It can be 0 or It can be 'x' or It can be '5'  
-----------
"""
############################

# ---------------
# Regular Expression PART-3
# ---------------
"""
# Custom Identifiers with exact data

abc[0-5].xyz  
    -> exact word 'abc' 
        followed by any one character b/n 0 to 5
        followed by any one any character. (Because it is .)
        followed by  exact word 'xyz'
-----------
"""
############################

# ---------------
# Regular Expression PART-4
# ---------------
r"""
# Quantifiers: We can specify quantity

[a-z]{3} -> any characters total 3 numbers
\d{3} -> any digit total 3 numbers
[a-z]{1, 3} -> Any character, it can be 1 numbers, 2 numbers or 3 numbers
\d{1, 3} -> any digit it can be 1 numbers, 2 numbers or 3 numbers

ab{2}c -> 'a' followed by exactly 2 times 'b' followed by 1 time c
[abc]{2} -> any one character in this group, that appears 2 times
            like aa or bb or cc
(abc){2} -> exact word 'abc' 2 times i.e 'abcabc'
-----------
"""
############################

# ---------------
# Regular Expression PART-5
# ---------------
"""
# Modifiers

* -> to tell 0 or more times
+ -> to tell 0 or 1 time
? -> to tell 0 or 1 time
-----------
"""
############################

# ---------------
# Regular Expression PART-6
# ---------------
"""
# Modifiers with examples

patten is: 'r[ea]d'

Meaning: r followed by any one character i.e it can be e or a then followed by d

input data:
rd # NO MATCH
red  # MATCH
rad  # MATCH
read  # NO MATCH
raed  # NO MATCH
raaaaaaad  # NO MATCH
reeeeeeeeed  # NO MATCH
raaaeeed  # NO MATCH
reeeaaad  # NO MATCH

-----------
"""
############################

# ---------------
# Regular Expression PART-7
# ---------------
"""
# Modifiers with examples

patten is: 'r(ea)d'

Meaning: r followed by exact word 'ea' then followed by d
    so this pattern, we can write only 'read'

input data:
rd # NO MATCH
red  # NO MATCH
rad  # NO MATCH
read  # MATCH
raed  # NO MATCH
raaaaaaad  # NO MATCH
reeeeeeeeed  # NO MATCH
raaaeeed  # NO MATCH
reeeaaad  # NO MATCH
-----------
"""
############################

# ---------------
# Regular Expression PART-8
# ---------------
"""
# Modifiers with examples

patten is: 'r(ea){2}d'

Meaning: r followed by exact word 'ea' 2 times then followed by d

input data:
rd # NO MATCH
red  # NO MATCH
rad  # NO MATCH
read  # NO MATCH
reaead  # MATCH
raed  # NO MATCH
raaaaaaad  # NO MATCH
reeeeeeeeed  # NO MATCH
raaaeeed  # NO MATCH
reeeaaad  # NO MATCH
-----------
"""
############################


# ---------------
# Regular Expression PART-9
# ---------------
"""
# Modifiers with examples

patten is: 'r[ea]*d'

Meaning: r followed by any ONE letter in this group [ea], 0 or more times

input data:
rd #  MATCH
red  # MATCH
rad  # MATCH
read  # NOT MATCH
reaead  # NOT MATCH
raed  #  NOT MATCH
raaaaaaad  #  MATCH
reeeeeeeeed  #  MATCH
raaaeeed  #  NOT MATCH
reeeaaad  #  NOT MATCH
-----------
"""
############################

# ---------------
# Regular Expression PART-10
# ---------------
"""
# Modifiers with examples

patten is: 'r(e|a)*d'

Meaning: r followed by any ONE letter in this group (e|a), 0 or more times

input data:
rd #  MATCH
red  # MATCH
rad  # MATCH
read  # MATCH
reaead  # MATCH
raed  #   MATCH
raaaaaaad  #  MATCH
reeeeeeeeed  #  MATCH
raaaeeed  #   MATCH
reeeaaad  #   MATCH
-----------
"""
############################


# ---------------
# Regular Expression PART-11
# ---------------
"""
# Modifiers with examples

patten is: 'r[ea]?d'

Meaning: r followed by any ONE letter in this group [ea], 0 or 1 time

input data:
rd #  MATCH
red  # MATCH
rad  # MATCH
read  # NO MATCH
reaead  # NO MATCH
raed  #   NO MATCH
raaaaaaad  #  NO MATCH
reeeeeeeeed  #  NO MATCH
raaaeeed  #   NO MATCH
reeeaaad  #   NO MATCH
-----------
"""
############################

print("Check only whether line is starting with IP address or not")
print("-"*20)
# ---------------

import re
for each_line in file_content:
    match_result = re.match(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d.*', each_line)
    # OR
    match_result = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.*', each_line)
    print("Each Line:", each_line)
    print("Match Result:", match_result, end="\n\n")
    print("-----------------")


print("#"*40, end="\n\n")
############################

print("Extract IP Address")
print("-"*20)
# ---------------

import re
for each_line in file_content:
     match_result = re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*', each_line)
     if match_result is not None:
        ip = match_result.group(1)
        print(ip)

r"""
put () to IP address pattern to capture
This is called grouping
each group will be having index number starting with 1
"""

print("#"*40, end="\n\n")
############################

print("Extract IP, DATE Address")
print("-"*20)
# ---------------

import re
for each_line in file_content:
    match_result = re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*(\d{2}/[A-Za-z]{3}/\d{4}).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        print(ip, dt)

r"""
Pattern for date: 26/Apr/2000

26
---
\d\d # Exactly 2 numbers
\d{2} # Exactly 2 numbers
[0-9][0-9] # Exactly 2 numbers
[0-9]{2} # Exactly 2 numbers
[0-9]\d # Exactly 2 numbers
\d[0-9] # Exactly 2 numbers

\d{1,2} # Minimum 1 time, maximum 2 times
[0-9]{1,2} # Minimum 1 time, maximum 2 times
\d?\d # Minimum 1 time, maximum 2 times
[0-9]?[0-9] # Minimum 1 time, maximum 2 times
\d?[0-9] # Minimum 1 time, maximum 2 times
[0-9]?\d # Minimum 1 time, maximum 2 times
---

Apr
----
[A-Z][a-z][a-z]
# OR
[A-Z][a-z]{2}
# OR
[a-zA-Z]{3}
# OR
(Jan|Feb|Mar)
----

"""

print("#"*40, end="\n\n")
############################

print("Extract IP, DATE, URL")
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

r"""
pattern for url: http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF

let us create custom identifier

http[s]?://[a-z./A-Z_]+

http[s]? -> s is optional
https? -> here also, s is optional
(https)? -> complete word 'https' is optional
[htttttttttps]? -> maximum one character can come in this group of characters [https], that too optional
    so, it can be 0 character
    or it can be 'h'
    or it can be 't'
    or it can be 'p'
    or it can be 's'

NOTE: Even though we have many time 't', it is counted as one 't' only

"""

print("#"*40, end="\n\n")
############################