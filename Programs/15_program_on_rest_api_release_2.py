"""
Developing rest-api using flask framework

Use Below 3 APIs for getting records from db
http://127.0.0.1:5000/myrestapi1
http://127.0.0.1:5000/myrestapi2
http://127.0.0.1:5000/myrestapi3

Use Below API for adding new record to db
http://127.0.0.1:5000/myrestapi4
"""


# -------------
# Create App
# -------------
import flask
my_rest_api_app = flask.Flask("MyAPIName")
##########################

# REST API-1:
#     - providing access to get data from 'mytable'
#     - END POINT: http://127.0.0.1:5000/myrestapi1
# -------------
# END POINT: http://127.0.0.1:5000/myrestapi1
# -------------
@my_rest_api_app.route("/myrestapi1", methods=["GET"])
def my_restapi1_function():
    import sqlite3
    my_db_connection = sqlite3.connect("mydb.db")
    my_db_cursor = my_db_connection.cursor()
    my_db_cursor.execute("select * from mytable")
    my_db_result = my_db_cursor.fetchall()
    my_db_connection.close()
    return flask.jsonify(my_db_result) # Convert to json and send
##########################

# REST API-2:
#     - providing access to get data from 'finalreporttable'
#     - END POINT: http://127.0.0.1:5000/myrestapi2
# -------------
# END POINT: http://127.0.0.1:5000/myrestapi2
# -------------
@my_rest_api_app.route("/myrestapi2", methods=["GET"])
def my_restapi2_function():
    import sqlite3
    my_db_connection = sqlite3.connect("mydb.db")
    my_db_cursor = my_db_connection.cursor()
    my_db_cursor.execute("select * from final_report_table")
    my_db_result = my_db_cursor.fetchall()
    my_db_connection.close()
    return flask.jsonify(my_db_result) # Convert to json and send
##########################

# REST API-3:
#     - providing access to get data from both 'finalreporttable' and "mytable"
#     - END POINT: http://127.0.0.1:5000/myrestapi3
# -------------
# END POINT: http://127.0.0.1:5000/myrestapi3
# -------------
@my_rest_api_app.route("/myrestapi3", methods=["GET"])
def my_restapi3_function():
    import sqlite3
    my_db_connection = sqlite3.connect("mydb.db")
    my_db_cursor = my_db_connection.cursor()

    my_db_cursor.execute("select * from mytable")
    mytable_db_data = my_db_cursor.fetchall()

    my_db_cursor.execute("select * from final_report_table")
    final_report_db_data = my_db_cursor.fetchall()

    my_db_connection.close()

    master_dictionary = {
    "My Table Data": mytable_db_data,
        "Final Report Table Date": final_report_db_data
    }

    return flask.jsonify(master_dictionary) # Convert to json and send
##########################


# REST API-4:
#     - providing access to add new record to 'mytable'
#     - END POINT: http://127.0.0.1:5000/myrestapi4
# -------------
# END POINT: http://127.0.0.1:5000/myrestapi4
# -------------
@my_rest_api_app.route("/myrestapi4", methods=["POST"])
def my_restapi4_function():
    """
    Assume end user will send new records in below format
    D = {"IP": "192.168.1.2", "DATE": "19/Feb/2026", "URL": "www.google.com"}

    Then our plan will be
    Task-1: Receive new record sent by end user
    Task-2: Check whether IP is already present in DB
    Task-3: Add new record to DB
    """
    # ------------------
    # Task-1: Receive new record sent by end user
    # ------------------
    new_record = flask.request.get_json()
    # Example: new_record = {"IP": "192.168.1.2", "DATE": "19/Feb/2026", "URL": "www.google.com"}
    ip = new_record["IP"]
    date = new_record["DATE"]
    url = new_record["URL"]
    #################################

    # ------------------
    # Task-2: Check whether IP is already present in DB
    # ------------------
    import sqlite3
    my_db_connection = sqlite3.connect("mydb.db")
    my_db_cursor = my_db_connection.cursor()
    my_query = f"select * from mytable where IP = '{ip}'"
    my_db_cursor.execute(my_query)
    my_db_result = my_db_cursor.fetchone() # returns None, if no record found
    if my_db_result is None:
        my_query = f"insert into mytable values('{ip}', '{date}', '{url}')"
        my_db_cursor.execute(my_query)
        my_db_connection.commit()
        my_db_connection.close()
        return flask.jsonify("New record added to DB")
    else:
        return flask.jsonify("Record is already present in DB")

    # Other option: SELECT COUNT(*) FROM MYTABLE WHERE IP = '123.123.123.123'
    #################################

##########################


# -------------
# Run builtin server
# -------------
my_rest_api_app.run()
# default host=127.0.0.1
# default port=5000
##########################