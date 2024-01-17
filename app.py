from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(host='',
                            database='',
                            user='',
                            password='')
    return conn


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/student_list")
def student_list():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM app_student;')
    students = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', students=students)
