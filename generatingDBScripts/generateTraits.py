from connectDB import db, cursor, saveDB, closeDB
import json

def generate():
     with open("data/5e-SRD-Traits.json", "r") as read_file:
          query = "INSERT INTO traits VALUES(NULL,%s, %s);"
          data = json.load(read_file)
          for traits in data:
               parameters = []
               _name = traits["name"]
               _desc = ""
               for desc in traits["desc"]:
                    _desc = _desc + desc
               parameters.append(_name)
               parameters.append(_desc)
               cursor.execute(query,parameters)



if __name__ == "__main__":
    generate()
    saveDB()
    closeDB()
