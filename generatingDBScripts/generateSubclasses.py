from connectDB import db, cursor, saveDB, closeDB
import json

def generate():
    with open("data/5e-SRD-Subclasses.json", "r") as read_file:
            querySubclasses = "INSERT INTO subclasses VALUES (%s,NULL,%s,%s,%s);"
            querySubclassFeatures  = "INSERT INTO subclassfeatures VALUES (NULL, %s, %s);"

            data = json.load(read_file)
            for subclass in data:
                _className = subclass['class']['name']
                _name = subclass['name']
                _subclassFlavor = subclass['subclass_flavor']
                _desc = ""
                for line in subclass['desc']:
                    _desc += (line + "\n")

                parameters = (_className, _name, _subclassFlavor, _desc)
                cursor.execute(querySubclasses, parameters)
                
                #------------features--------------
                for feature in subclass['features']:
                        _idFeature = feature['url'].split("/")[-1]
                        parameters = (_className, _idFeature)
                        cursor.execute(querySubclassFeatures, parameters)


if __name__ == "__main__":
    generate()
    saveDB()
    closeDB()