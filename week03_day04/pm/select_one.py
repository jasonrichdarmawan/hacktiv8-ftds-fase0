import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="my-secret-pw",
  database="ftds"
)

cursor = db.cursor()
sql = "SELECT * FROM student"
cursor.execute(sql)

result = cursor.fetchone()

print(result)