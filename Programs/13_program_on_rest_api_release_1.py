"""
Developing rest-api using flask framework
"""

"""
Example to understand what is API?

Suppose, we want to provide access to our database mydb.db with others/public
then how can we provide access to our database mydb.db with others/public?

One option is, we can create separate credentials like username/password etc
with restricted permissions and share credentials with others/public.

This option will not work when come to public or others.
"""

"""
We got other ways.

We got 2 solutions
1. SOAP : Simple Object Access Protocol
2. REST : REpresentational State Transfer

Both are called architecture/style/designs 
Both tells, how can we provide access to others/public

Both tells, provide some MAIN-DOOR/INTERFACE to our application/resource/db
like
our application/resource/db   <-INTERFACE->  others/public

This INTERFACE is also called as APPLICATION PROGRAMMING INTERFACE (API)

Both tells how to implement INTERFACE/API
"""

"""
REST came after SOAP
REST is easy to implement and manage
REST is popular
"""

"""
How to implement REST architecture to create API?
- No need to implement REST architecture from the scratch
    because we have many frameworks which already implemented
    REST architecture. Frameworks like flask, fast-api, django etc
- So, we just need to know, how to create api using any of the framework.
"""

"""
Popular frameworks in python
1. fast-api
    https://fastapi.tiangolo.com/tutorial/first-steps/
2. flask
    https://pypi.org/project/Flask/
3. DJango
    https://pypi.org/project/Django/
"""

"""
In web development, mainly we do
1. Developing websites
2. Developing API
3. Developing microservices
"""

"""
What we can do using below frameworks?

1. fast-api 

    - small framework where we can maintain all front-end/back-end/db etc code in one file

    We can do 2 things using fast-api
    - Developing API
    - Developing microservices    

2. flask 
    - small framework where we can maintain all front-end/back-end/db etc code in one file

    We can do 3 things using flask

    - Developing websites
    - Developing API
    - Developing microservices

3. DJango 
    - BIG framework/MVT framework: Model View Template
    - where we can maintain all front-end/back-end/db etc in SEPARATE files

    We can do 3 things using django

    - Developing websites
    - Developing API
    - Developing microservices  

"""

"""
We want to develop REST-API to provide COMPLETE-ACCESS/FULL-ACCESS
to our tables.

COMPLETE-ACCESS/FULL-ACCESS means
1. We need to provide access to CREATE / add new record in our table
2. We need to provide access to READ / get existing records from our table
3. We need to provide access to UPDATE existing records in our table
4. We need to provide access to DELETE existing records from our table
"""

"""
We have something like HTTP worldwide standards
- For API, we need to manage some HTTP standard like http-methods (GET/POST/PUT/PATCH/DELETE)
"""

"""
Http method we need to specify for our requirement is

1. We need to provide access to CREATE / add new record in our table
    - Here we need to use http method POST

2. We need to provide access to READ / get existing records from our table
    - Here we need to use http method GET

3. We need to provide access to UPDATE existing records in our table
    - Here we need to use http method PUT/PATCH
    - PUT: use this if we are providing option to update entire row in a table
    - PATCH: use this if we are providing option to update few fields in a row in a table
        like update only email-id, update only address-field

4. We need to provide access to DELETE existing records from our table
    - Here we need to use http method DELETE
"""

"""
About web server:

- To run any web-application(website/api/microservices)
    we need web-server

- flask is having one small server which we can use it for development purpose
    we can't use this for production deployment
"""

"""
In this release, we are planning provide access get all records from both tables

We need following URLs, also called END POINTS

REST API-1: 
    - providing access to get data from 'mytable'
    - END POINT: http://127.0.0.1:5000/myrestapi1

REST API-2: 
    - providing access to get data from 'finalreporttable'
    - END POINT: http://127.0.0.1:5000/myrestapi2

REST API-3: 
    - providing access to get data from both 'finalreporttable' and "mytable"
    - END POINT: http://127.0.0.1:5000/myrestapi3
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
# END POINT: http://127.0.0.1:
# 5000/myrestapi1
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

# http://127.0.0.1:5000/myrestapi1
# http://127.0.0.1:5000/myrestapi2
# http://127.0.0.1:5000/myrestapi3

# -------------
# Run builtin server
# -------------
my_rest_api_app.run()
# default host=127.0.0.1
# default port=5000
##########################

