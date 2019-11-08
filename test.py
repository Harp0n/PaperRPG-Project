import mysql.connector
import json 


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Biedro123",
  database='RPG',
  auth_plugin='mysql_native_password'
)
cursor = mydb.cursor()


add_language = "INSERT INTO languages VALUES (NULL,%s,%s,%s))

with open("5e-SRD-Languages.json", "r") as read_file:
    languageArray = json.load(read_file)
    for language in languageArray:
        _name = language['name']
        _type = language['type']
        _script = language['script']
        



##command = ("""INSERT INTO languages VALUES (NULL, 'Common', 'Standard', 'Common');""")
##cursor.execute(command)
##
##
##
##
##
##mydb.commit()

cursor.close()
mydb.close()
