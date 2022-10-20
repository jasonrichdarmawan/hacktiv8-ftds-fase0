import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="my-secret-pw"
)

if db.is_connected():
  print("Successfully connected to MySQL database")