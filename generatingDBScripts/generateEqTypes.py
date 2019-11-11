from connectDB import db, cursor, saveDB, closeDB
import json

def generate():
     with open("data/5e-SRD-Equipment-Categories.json", "r") as read_file:
          query = "INSERT INTO equipmentcategories VALUES(NULL,%s);"
          data = json.load(read_file)
          for eqCat in data:
               parameters = []
               _category = eqCat["name"]
               parameters.append(_category)
               cursor.execute(query,parameters)



if __name__ == "__main__":
    generate()
    saveDB()
    closeDB()
