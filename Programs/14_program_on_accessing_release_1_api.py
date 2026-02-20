"""
Accessing below API end points using 'requests' library

http://127.0.0.1:5000/myrestapi1
http://127.0.0.1:5000/myrestapi2
http://127.0.0.1:5000/myrestapi3
"""

print("Accessing myrestapi1")
print("-"*20)
# ---------------

try:
    import requests
    api_response = requests.get("http://127.0.0.1:5000/myrestapi1")
    myrestapi1_data = api_response.json()
    print(myrestapi1_data)
except Exception as e:
    print("Not Able To Access myrestapi1: Reason is:", e, sep="\n", end="\n\n")
    print("""
    Please make sure to run '13_program_on_rest_api_release_1.py' 
    before running this program.""")
    exit()

print("#"*40, end="\n\n")
############################

print("Accessing myrestapi2")
print("-"*20)
# ---------------

try:
    import requests
    api_response = requests.get("http://127.0.0.1:5000/myrestapi2")
    myrestapi2_data = api_response.json()
    print(myrestapi2_data)
except Exception as e:
    print("Not Able To Access myrestapi2: Reason is:", e, sep="\n", end="\n\n")
    print("""
    Please make sure to run '13_program_on_rest_api_release_1.py' 
    before running this program.""")
    exit()

print("#"*40, end="\n\n")
############################

print("Accessing myrestapi3")
print("-"*20)
# ---------------

try:
    import requests
    api_response = requests.get("http://127.0.0.1:5000/myrestapi3")
    myrestapi3_data = api_response.json()
    print(myrestapi3_data)
except Exception as e:
    print("Not Able To Access myrestapi3: Reason is:", e, sep="\n", end="\n\n")
    print("""
    Please make sure to run '13_program_on_rest_api_release_1.py' 
    before running this program.""")
    exit()

print("#"*40, end="\n\n")
############################