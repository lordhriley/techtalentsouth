#!/usr/bin/python3

# tutorial - https://www.tutorialspoint.com/python3/python_database_access.htm

import pymysql

# Open database connection
db = pymysql.connect("localhost", "root", "Gary1973!", "employees")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,  
   SEX CHAR(1),
   INCOME FLOAT )"""

cursor.execute(sql)

# disconnect from server
db.close()

# mysql command line
# use employees;
# show tables;
