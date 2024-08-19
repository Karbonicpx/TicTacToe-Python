import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Nicolas@'
); # Acessing mysql server

myrcursor = mydb.cursor() # Object that will comunicate with the database

