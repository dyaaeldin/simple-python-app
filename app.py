#!/usr/bin/env python

import sys
import _mysql
from flask import Flask
import MySQLdb as mdb

DB_HOST = os.environ[MYSQL_HOST]
DB_USER = os.environ[MYSQL_USER]
DB_PASSWORD = os.environ[MYSQL_PASSWORD]
DB_NAME = os.environ[MYSQL_DBNAME]

mydb = mysql.connector.connect(
  host=DB_HOST,
  user=DB_USER,
  password=DB_PASSWORD
)

app = Flask(__name__)

@app.route("/")
def hello():
    return mydb

if __name__ == "__main__":
    app.run()