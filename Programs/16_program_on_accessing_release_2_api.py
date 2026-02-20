"""
Accessing below API end points using 'requests' library

# Below rest apis are for getting records from database
http://127.0.0.1:5000/myrestapi1
http://127.0.0.1:5000/myrestapi2
http://127.0.0.1:5000/myrestapi3

# Below api is to add new record to database
http://127.0.0.1:5000/myrestapi4
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
    Please make sure to run '15_program_on_rest_api_release_2.py' 
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
    Please make sure to run '15_program_on_rest_api_release_2.py' 
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
    Please make sure to run '15_program_on_rest_api_release_2.py' 
    before running this program.""")
    exit()

print("#"*40, end="\n\n")
############################

print("Accessing myrestapi4 for adding new records to database")
print("-"*20)
# ---------------

try:
    import requests
    api_response = requests.post("http://127.0.0.1:5000/myrestapi4",
                                 json={"IP": "192.168.1.2", "DATE": "19/Feb/2026", "URL": "www.google.com"}
                                 )
    myrestapi1_data = api_response.json()
    print(myrestapi1_data)
except Exception as e:
    print("Not Able To Access myrestapi1: Reason is:", e, sep="\n", end="\n\n")
    print("""
    Please make sure to run '15_program_on_rest_api_release_2.py' 
    before running this program.""")
    exit()

print("#"*40, end="\n\n")
############################