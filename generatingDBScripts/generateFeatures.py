from connectDB import db, cursor, saveDB, closeDB
import json

def generate():
    with open ("data/5e-SRD-Features.json") as read_file:
        query = "INSERT INTO features VALUES (NULL,%s,%s,%s,%s,%s)"        
        data = json.load(read_file)
        for feature in data:
            parameters = []
            _className = feature["class"]["name"]
            parameters.append(_className)
            parameters.append(feature["name"])
            if('level' in feature):
                parameters.append(feature['level'])
            else:
                parameters.append(0)           
            desc=''
            for line in feature["desc"]:
                desc += (line + "\n")
            parameters.append(desc)
            if(len(feature["name"]) > 45): 
                print(feature["name"] + " " + str(len(feature["name"])) + "\n")
            if('choice' in feature):
                parameters.append(feature["choice"]["choose"])
            else:
                parameters.append(0)
            parameters = tuple(parameters)
            cursor.execute(query,parameters)



if __name__ == "__main__":
    generate()
    saveDB()
    closeDB()


