from connectDB import db, cursor, saveDB, closeDB
import json

def generate():
    with open("data/5e-SRD-Proficiencies.json", "r") as read_file:
        query = "INSERT INTO proficiences VALUES (NULL,%s,%s);"
        data = json.load(read_file)
        for proficiency in data:
            _type = proficiency['type']
            _name = proficiency['name']
            parameters = (_type, _name)
            cursor.execute(query,parameters)

if __name__ == "__main__":
    generate()
    saveDB()
    closeDB()