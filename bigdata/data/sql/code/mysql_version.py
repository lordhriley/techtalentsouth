# change MAC OS paths
# sudo nano /etc/paths

# brew install mysql
# brew services start mysql
# brew services stop mysql

# mysql -uroot
# mysql_secure_installation # to change password for root

# brew unlink mysql
# brew install mysql-connector-c

# Add the mysql bin folder to PATH
# export PATH=/usr/local/Cellar/mysql/8.0.11/bin:$PATH
# mkdir /usr/local/Cellar/lib/

# Create a symlink
# sudo ln -s /usr/local/Cellar/mysql/8.0.21/lib/libmysqlclient.21.dylib /usr/local/Cellar/lib/libmysqlclient.21.dylib
# brew reinstall openssl (source)

# brew link mysql

# Finally, install mysql-client
# LIBRARY_PATH=$LIBRARY_PATH:/usr/local/opt/openssl/lib/ pip3 install mysqlclient

# ---

# command line
# mysql -uroot -p

# create database employees;
# show databases;

#!/usr/bin/python3
# -*- coding: utf-8 -*-

# pip3 install mysql.connector
# pip3 install crytography
# git clone https://github.com/PyMySQL/PyMySQL
# sudo python3 setup.py install.

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql

#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost", "root", "Gary1973!", "employees")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Database version : %s " % data)

# disconnect from server
db.close()
