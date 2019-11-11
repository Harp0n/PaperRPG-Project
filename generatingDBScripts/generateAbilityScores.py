from connectDB import db, cursor, saveDB, closeDB
import json

def generate():
    with open("data/5e-SRD-Ability-Scores.json", "r") as read_file:
        query = "INSERT INTO abilities VALUES (NULL,%s,%s,%s);"
        data = json.load(read_file)
        for proficiency in data:
            parameters = []
            parameters.append(proficiency['name'])
            parameters.append(proficiency['full_name'])
            desc = ""
            for line in proficiency['desc']:
                desc += (line + "\n")
            parameters.append(desc)
            parameters = tuple(parameters)
            cursor.execute(query,parameters)

if __name__ == "__main__":
    generate()
    saveDB()
    closeDB()