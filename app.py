# Author: Catalina Escalona
# Date: 2023-11-07
# Lab 10, CSPB 3308, Fall 2023

from flask import Flask
import psycopg2

app = Flask(__name__)

# index route listing all possible routes for lab 10
@app.route('/')
def hello_world():
    resp = '''
        Hello, World!<br><br>
        Author: Catalina Escalona<br>
        Date: 2023-11-07<br>
        Lab 10, CSPB 3308, Fall 2023<br><br>
        <h3>All Routes Supported:</h3>
        /<br>
        /db_test<br>
        /db_create<br>
        /db_insert<br>
        /db_select<br>
        /db_drop<br>
        '''
    return resp

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

# a route to populate the table in database
@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgres://catalina_lab_10_db_user:yPo6HWW8sTwX2D7cBG2DcqXyyDLVGg1l@dpg-cl53dnil7jac73cb8vo0-a/catalina_lab_10_db")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

# a route to query from the table in database
@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgres://catalina_lab_10_db_user:yPo6HWW8sTwX2D7cBG2DcqXyyDLVGg1l@dpg-cl53dnil7jac73cb8vo0-a/catalina_lab_10_db")
    cur = conn.cursor()
    cur.execute('''
       SELECT * FROM Basketball;
        ''')
    records = cur.fetchall()
    conn.close()
    response_string=""
    response_string+="<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
        response_string+="</tr>"
    response_string+="</table>"
    return response_string

# a route to drop the table in database
@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgres://catalina_lab_10_db_user:yPo6HWW8sTwX2D7cBG2DcqXyyDLVGg1l@dpg-cl53dnil7jac73cb8vo0-a/catalina_lab_10_db")
    cur = conn.cursor()
    cur.execute('''
       DROP TABLE Basketball;
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"