"""
Get data from sample_data.txt

then

extract
IP
DATE
URL

then write extracted information to my_report_1.txt

Expected content in my_report_1.txt
        IP                          DATE                        URL
123.123.123.123         26/Apr/2000         http://www.jafsoft.com/asctortf/
123.123.123.123         26/Apr/2000         http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF
123.123.123.123         26/Apr/2000         http://www.jafsoft.com/asctortf/
123.123.123.123         26/Apr/2000         http://www.jafsoft.com/asctortf/
123.123.123.123         26/Apr/2000         http://www.jafsoft.com/asctortf/
123.123.123.123         26/Apr/2000         http://www.jafsoft.com/asctortf/
"""

"""
Get data from sample_data.txt

then

extract
IP
DATE
URL

then write extracted information to my_report_1.txt

Expected content in my_report_1.txt
        IP                          DATE                        URL
123.123.123.123         26/Apr/2000         http://www.jafsoft.com/asctortf/
123.123.123.123         26/Apr/2000         http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF
123.123.123.123         26/Apr/2000         http://www.jafsoft.com/asctortf/
123.123.123.123         26/Apr/2000         http://www.jafsoft.com/asctortf/
123.123.123.123         26/Apr/2000         http://www.jafsoft.com/asctortf/
123.123.123.123         26/Apr/2000         http://www.jafsoft.com/asctortf/
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

print("Access each line and print")
print("-"*20)
# ---------------

for each_line in file_content_list:
    print("Each Line:", each_line)
    print("Type of Each Line:", type(each_line), end="\n\n")

print("#"*40, end="\n\n")
############################

print("print IP address lines")
print("-"*20)
# ---------------

for each_line in file_content_list:
    if each_line.startswith("123"):
        print("Each Line:", each_line)

print("#"*40, end="\n\n")
############################

print("Extract IP: 1-way: PARTIAL")
print("-"*20)
# ---------------

# sample_line = 123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"

for each_line in file_content_list:
    if each_line.startswith("123"):
        ip = each_line[0:15]
        print(ip)

print("#"*40, end="\n\n")
############################

# ---------------
# Example-1
# ---------------
# >>> # startswith() method example
# >>> my_string = "123.123.123.123. sdjkadsksa"
# >>> my_string.startswith("123")
# True
############################

# ---------------
# Example-2
# ---------------
# >>> # Learning find() method
# >>> # feature-1
# >>> my_string = "WEL COME"
# >>> my_string.find("E") # returns index of 1st occurance of "E"
# 1
# >>> # feature-2
# >>> my_string = "WEL COME"
# >>> my_string.find("E", 3) # returns index of "E" which is coming after 3rd index
# 7
# >>> # feature-3
# >>> my_string = "WEL COME"
# >>> my_string.find("COME") # returns index of 'C'
# 4
# >>> # feature-4
# >>> my_string = "WEL COME"
# >>> my_string.find("XYZ")
# -1
############################

print("Extract IP: 2-way")
print("-"*20)
# ---------------

# sample_line = 123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"

for each_line in file_content_list:
    if each_line.startswith("123"):
        start_index = 0
        end_index = each_line.find(" ")
        ip = each_line[start_index:end_index]
        print(ip)

print("#"*40, end="\n\n")
############################


print("Extract IP: 3-way")
print("-"*20)
# ---------------

# sample_line = 123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"

for each_line in file_content_list:
    if each_line.startswith("123"):
        sp = each_line.split(" ")
        # print("sp:", sp)
        ip =sp[0]
        print(ip)

print("#"*40, end="\n\n")
############################

print("Extract DATE: 1-way")
print("-"*20)
# ---------------

# sample_line = 123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"

for each_line in file_content_list:
    if each_line.startswith("123"):

        # IP
        start_index = 0
        end_index = each_line.find(" ")
        ip = each_line[start_index:end_index]

        # DATE
        start_index = each_line.find("[")
        start_index = start_index + 1
        end_index = each_line.find(":")
        dt = each_line[start_index:end_index]
        print(ip, dt)

print("#"*40, end="\n\n")
############################

print("Extract DATE: 2-way")
print("-"*20)
# ---------------

# sample_line = 123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"

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

        print(ip, dt)

print("#"*40, end="\n\n")
############################

print("Extract URL: 1-way")
print("-"*20)
# ---------------

# sample_line = 123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"

for each_line in file_content_list:
    if each_line.startswith("123"):

        # IP
        start_index = 0
        end_index = each_line.find(" ")
        ip = each_line[start_index:end_index]

        # DATE
        start_index = each_line.find("[")
        start_index = start_index + 1
        end_index = each_line.find(":")
        dt = each_line[start_index:end_index]

        # URL
        start_index = each_line.find("http") # returns index of 'h'
        end_index = each_line.find('"', start_index)
        url = each_line[start_index:end_index]

        print(ip, dt, url)

print("#"*40, end="\n\n")
############################

print("Extract URL: 2-way")
print("-"*20)
# ---------------

# sample_line = 123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"

for each_line in file_content_list:
    if each_line.startswith("123"):
        sp = each_line.split(" ")
        print("sp:", sp)

        # IP
        ip =sp[0]

        # DATE
        raw_date = sp[3] # '[26/Apr/2000:00:23:48'

        start_index = 1
        end_index = raw_date.find(":")
        dt = raw_date[start_index:end_index]

        raw_url = sp[10] # '"http://www.jafsoft.com/asctortf/"'
        # in url: 1st and last character is ", which we need to remove

        # 1-way to Remove " from both the sides of url:  '"http://www.jafsoft.com/asctortf/"'
        url1 = raw_url[1 : len(raw_url)-1]

        # 2-way to Remove " from both the sides of url:  '"http://www.jafsoft.com/asctortf/"'
        url2 = raw_url[1 : -1]

        # 3-way to Remove " from both the sides of url:  '"http://www.jafsoft.com/asctortf/"'
        url3_sp = raw_url.split('"')
        print("url3_sp:", url3_sp) # ['', 'http://www.jafsoft.com/asctortf/', '']
        url3 = url3_sp[1]

        # 4-way to Remove " from both the sides of url:  '"http://www.jafsoft.com/asctortf/"'
        url4 = raw_url.strip('"') # ' " '
        # strip will remove only at the ends

        # 5-way to Remove " from both the sides of url:  '"http://www.jafsoft.com/asctortf/"'
        url5 = raw_url.replace('"', '')
        # replace " with empty string
        # IMPORTANT: replace will replace all occurances present in entire data

        # 6-way to Remove " from both the sides of url:  '"http://www.jafsoft.com/asctortf/"'
        url6 = raw_url.removeprefix('"') # remove " from beginning and store in url6
        url6 = url6.removesuffix('"')

        # 7-way to Remove " from both the sides of url:  '"http://www.jafsoft.com/asctortf/"'
        url7 = raw_url.removeprefix('"').removesuffix('"')

        print(ip, dt, url1, url2, url3, url4, url5, url6, url7)

print("#"*40, end="\n\n")
############################

print("write extracted information to my_report_1.txt")
print("-"*20)
# ---------------

my_file_handle = open(file="my_report_1.txt", mode="w")

print("IP", "DATE", "URL", sep="\t",file=my_file_handle)

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

        print(ip, dt, url, sep="\t", file=my_file_handle)

my_file_handle.close()

print("Created my_report_1.txt file, Please check")

print("#"*40, end="\n\n")
############################