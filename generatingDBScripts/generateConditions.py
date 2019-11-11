import re
import json
from connectDB import db, cursor, saveDB, closeDB

def generate():
    with open("data/5e-SRD-Conditions.json", "r") as read_file:
        query = "INSERT INTO conditions VALUES (NULL,%s,%s);"
        data = json.load(read_file)
        for condition in data:
            parameters = []
            desc=""
            parameters.append(condition["name"])
            for line in condition["desc"]:
                desc += (line + "\n")
            parameters.append(desc)
            parameters = tuple(parameters)
            cursor.execute(query,parameters)


if __name__ == "__main__":
    generate()
    saveDB()
    closeDB()

