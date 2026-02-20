"""
Since we are using more than one function for one-task
that is log_process. So, if it is more than one function to write
for particular task then we need to write class.
"""

"""
Write class called 'LogProcessClass' which is having below methods

# Expected Output

l1 = LogProcessClass("sample_data.txt")

all_ips = l1.get_ips() 
print(all_ips) # ['ip1', 'ip2']

all_data = l1.extract_all_info()
print(all_data) # return dictionary

l1.write_to_text_file("my_output_file.txt") # This should write all content to my_output_file.txt

l1.write_to_json_file("my_output_file.json") # This should write all content to my_output_file.json

"""

print("Writing 'LogProcessClass'")
print("-"*20)
# ---------------

class LogProcessClass:
    def __init__(self, input_file_path):
        my_file_handle = open(file=input_file_path, mode="r")
        self.input_file_content = my_file_handle.readlines()
        my_file_handle.close()

    def get_all_ips(self):
        all_ips = []
        for each_line in self.input_file_content:
            if each_line.startswith("123"):
                sp = each_line.split(" ")
                ip = sp[0]
                all_ips.append(ip)
        return all_ips

    def extract_all_info(self):
        my_list = []
        for each_line in self.input_file_content:
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
                my_list.append(each_line_tuple)
        return my_list
    def write_to_text_file(self, output_file_path):
        data = self.extract_all_info()
        # data = [(ip, dt, url), (ip, dt, url), (ip, dt, url),]
        my_output_file_handle = open(file=output_file_path, mode="w")
        print("IP", "DATE", "URL", sep="\t", file=my_output_file_handle)
        for each_line_tuple in data:
            # each_line_tuple = (ip, dt, url)
            ip = each_line_tuple[0]
            date = each_line_tuple[1]
            url = each_line_tuple[2]
            print(ip, date, url, sep="\t", file=my_output_file_handle)
        my_output_file_handle.close()
    def write_to_json_file(self, output_file_path):
        data = self.extract_all_info()
        my_output_file_handle = open(file=output_file_path, mode="w")
        import json
        json.dump(data, my_output_file_handle)
        my_output_file_handle.close()

print("#"*40, end="\n\n")
############################

print("Testing LogProcessClass")
print("-"*20)
# ---------------

my_log_1_object = LogProcessClass("sample_data.txt")
all_ips = my_log_1_object.get_all_ips()
print("all_ips", all_ips, end="\n\n")

all_info = my_log_1_object.extract_all_info()
print("all_info", all_info, end="\n\n")

my_log_1_object.write_to_text_file("my_report_7.txt")
print("File my_report_7.txt created", end="\n\n")

my_log_1_object.write_to_json_file("my_report_8.json")
print("File my_report_8.json created", end="\n\n")

print("#"*40, end="\n\n")
############################