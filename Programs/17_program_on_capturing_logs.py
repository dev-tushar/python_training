"""
Program on capturing logs using logging library
logging library: https://docs.python.org/3/library/logging.html
"""

print("Configure my_logger")
print("-"*20)
# ---------------

import logging

logging.basicConfig(filename="mylog.log",
                    filemode="w",
                    level=logging.DEBUG,
                    format="%(levelname)s : %(asctime)s : %(filename)s : %(message)s"
                    )
my_logger = logging.getLogger("my_logger")

print("Configuring my_logger is don. Now we can use my_logger to write to file")

print("#"*40, end="\n\n")
############################


print("Test whether my_logger is writing to file")
print("-"*20)
# ---------------

my_logger.info("This is my INFO message") # write to file
my_logger.warning("This is my WARNING message") # write to file
my_logger.error("This is my ERROR message") # write to file
my_logger.critical("This is my CRITICAL message") # write to file
my_logger.debug("This is my DEBUG message") # write to file

print("Test messages are captured in mylog.log. Please check")

print("#"*40, end="\n\n")
############################

print("Accessing myrestapi1")
print("-"*20)
# ---------------

my_logger.info("Accessing myrestapi1")

try:
    my_logger.info("Importing requests library")
    import requests
    my_logger.info("Requests library imported is SUCCESS")

    my_logger.info("Accessing myrestapi1")
    api_response = requests.get("http://127.0.0.1:5000/myrestapi1")
    my_logger.info("Accessing myrestapi1 is SUCCESS")

    my_logger.info("Getting data from api_response")
    myrestapi1_data = api_response.json()
    my_logger.info("Getting data from api_response is SUCCESS")

    my_logger.info("printing data in console using print() function")
    print(myrestapi1_data)
    my_logger.info("printing data in console using print() function SUCCESS")

except Exception as e:

    my_logger.error(f"Not Able To Access myrestapi1: Reason is: {e}")

    my_logger.info("""Please make sure to run '15_program_on_rest_api_release_2.py' 
    before running this program.""")
    my_logger.info("Manually existing the program using exit() function")
    exit()
finally:
    print("Logs captured in mylog.log. Please check")

print("#"*40, end="\n\n")
############################