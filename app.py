# Author: Catalina Escalona
# Date: 2023-11-07
# Lab 10, CSPB 3308, Fall 2023

from flask import Flask
import psycopg2

app = Flask(__name__)

# starter route (from Render's "Deploy a Flask App" tutorial)
@app.route('/')
def hello_world():
    return 'Hello, World!'

# a route to check if database connection works
@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://catalina_lab_10_db_user:yPo6HWW8sTwX2D7cBG2DcqXyyDLVGg1l@dpg-cl53dnil7jac73cb8vo0-a/catalina_lab_10_db")
    conn.close()
    return "Database Connection Successful"

# a route to create a new table in database
@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgres://catalina_lab_10_db_user:yPo6HWW8sTwX2D7cBG2DcqXyyDLVGg1l@dpg-cl53dnil7jac73cb8vo0-a/catalina_lab_10_db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"