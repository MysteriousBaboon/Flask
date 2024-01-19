from flask import Flask, render_template
import psycopg2
import os
import boto3
from PIL import Image
import io

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def get_db_connection():
    conn = psycopg2.connect(host='mark.cfas4wq4cb4x.eu-west-3.rds.amazonaws.com',
                            database='postgres',
                            user='postgres',
                            password='CGKKM4JejXYQ5PIRgC8a')
    return conn


@app.route("/student_list")
def student_list():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM app_student;')
    students = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', students=students)


@app.route('/pinguin_and_poney')
def pinguin_and_poney():
    s3 = boto3.client('s3')
    s3.download_file('bucketanuno', 'drapeau-anne-stokes-pirate-pr.png', 'nuno2.png')
    return "<p>Chouette le poney!</p>"

@app.route('/test')
def pinguin_and_poney():
    return "<p>TEST!</p>"
