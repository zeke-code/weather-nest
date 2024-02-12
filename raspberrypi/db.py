import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='pythonUser',
    password='pythonPWD',
    database='weather'
)

cursor = db.cursor()