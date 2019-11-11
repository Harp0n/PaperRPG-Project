from connectDB import db, cursor, saveDB, closeDB
import json

def generate():
     with open("data/5e-SRD-Magic-Schools.json", "r") as read_file:
          query = "INSERT INTO magicschools VALUES(NULL,%s, %s);"
          data = json.load(read_file)
          for magicSchools in data:
               parameters = []
               _category = magicSchools["name"]
               _desc = magicSchools["desc"]
               parameters.append(_category)
               parameters.append(_desc)
               cursor.execute(query,parameters)



if __name__ == "__main__":
    generate()
    saveDB()
    closeDB()
