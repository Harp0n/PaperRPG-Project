from connectDB import db, cursor, saveDB, closeDB
import json



def generate():
    with open("data/5e-SRD-Skills.json", "r") as read_file:
        query = "INSERT INTO skills VALUES (%s, NULL,%s,%s);"
        data = json.load(read_file)
        for skill in data:
            _name = skill["name"]
            print(_name)
            _desc = ""
            for desc in skill["desc"]:
                _desc += desc
            _api = skill["ability_score"]["url"].split("/")[-1]
            parameters = (_name , _desc, _api)
            cursor.execute(query, parameters)
            
            
                
        

if __name__ == "__main__":
    generate()
    saveDB()
    closeDB()
