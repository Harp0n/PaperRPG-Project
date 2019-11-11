import re
import json
from connectDB import db, cursor, saveDB, closeDB


def generate():
    with open ("data/5e-SRD-Languages.json", "r") as read_file:
        query = "INSERT INTO languages VALUE (NULL,%s,%s);"
        data = json.load(read_file)
        for language in data:
            parameters = []
            parameters.append(language["name"])
            parameters.append(language["type"])
            cursor.execute(query,parameters)


if __name__ == "__main__":
    generate()
    saveDB()
    closeDB()