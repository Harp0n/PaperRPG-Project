import mysql.connector
import json 


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="haslo1",
  database='RPG',
  auth_plugin='mysql_native_password'
)
cursor = mydb.cursor()

addLanguageTable = """CREATE TABLE IF NOT EXISTS `languages` (
	`id` int(10) NOT NULL AUTO_INCREMENT,
	`name` varchar(255),
	`type` varchar(255),
	`script` varchar(255),
	PRIMARY KEY( `id` )
);"""

def addTables():
    cursor.execute("DROP TABLE IF EXISTS languages;")
    cursor.execute(addLanguageTable)

addTables()

    



add_language = "INSERT INTO languages VALUES (NULL,%s,%s,%s);"

with open("data/5e-SRD-Languages.json", "r") as read_file:
    languageArray = json.load(read_file)
    for language in languageArray:
        _name = language['name']
        _type = language['type']
        _script = language['script']
        cursor.execute(add_language, (_name, _type, _script))
        



##command = ("""INSERT INTO languages VALUES (NULL, 'Common', 'Standard', 'Common');""")
##cursor.execute(command)





mydb.commit()

cursor.close()
mydb.close()
