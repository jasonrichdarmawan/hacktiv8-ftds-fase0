import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="my-secret-pw"
)

if db.is_connected():
  print("Successfully connected to MySQL database")
else:
  exit()

cursor = db.cursor()

cursor.execute("CREATE DATABASE ftds")
print("Dabase successfully created")