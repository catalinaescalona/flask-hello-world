from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://catalina_lab_10_db_user:yPo6HWW8sTwX2D7cBG2DcqXyyDLVGg1l@dpg-cl53dnil7jac73cb8vo0-a/catalina_lab_10_db")
    conn.close()
    return "Database Connection Successful"