import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="haslo1",
  database='RPG',
  auth_plugin='mysql_native_password'
)

cursor = db.cursor()

def saveDB():
  db.commit()
def closeDB():
  cursor.close()
  db.close()