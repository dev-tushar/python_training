"""
Read and print website data
Library: requests
Library Documentation: https://pypi.org/project/requests/#description
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