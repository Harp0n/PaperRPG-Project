from connectDB import db, cursor, saveDB, closeDB
import json

def generate():
    with open("data/5e-SRD-Damage-Types.json", "r") as read_file:
        query = "INSERT INTO damageTypes VALUES (NULL,%s,%s);"
        data = json.load(read_file)
        for damageType in data:
            _name = damageType['name']
            _desc = ""
            for line in damageType['desc']:
                _desc += (line + "\n")
            parameters = (_name, _desc)
            cursor.execute(query,parameters)

if __name__ == "__main__":
    generate()
    saveDB()
    closeDB()