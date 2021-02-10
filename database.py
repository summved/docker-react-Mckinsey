#!/usr/bin/python

import MySQLdb

# Open database connection
usesr_to_db="dbuser"
password_to_db="randompasswordassigntomydb"
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7R5K1RAW"
db = MySQLdb.connect("localhost",usesr_to_db,password_to_db,"TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print "Database version : %s " % data

# disconnect from server
db.close()