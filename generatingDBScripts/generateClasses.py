from connectDB import db, cursor, saveDB, closeDB
import json

def generate():
    with open("data/5e-SRD-Classes.json", "r") as read_file:
            queryClasses = "INSERT INTO classes VALUES (NULL,%s,%s,%s);"
            queryClassProficiences = "INSERT INTO classproficiencies VALUES (NULL,%s,%s,%s);"
            queryClassSavingThrows = "INSERT INTO classsavingthrows VALUES (NULL,%s,%s);"
            queryClassSubclasses = "INSERT INTO classsubclasses VALUES (NULL,%s,%s);"
            data = json.load(read_file)
            for c in data:
                _idClass = c['index']
                _name = c['name']
                _hitDie = c['hit_die']
                if("choose" in c['proficiency_choices'][0]):
                    _proficiencyChoicesCount = c['proficiency_choices'][0]['choose']
                else:
                    _proficiencyChoicesCount = 0
                parameters = (_name, _hitDie, _proficiencyChoicesCount)
                cursor.execute(queryClasses, parameters)
                #------------proficiencies--------------
                if('from' in c['proficiency_choices'][0]):
                    for proficiency in c['proficiency_choices'][0]['from']:
                        _idProficiency = proficiency['url'].split("/")[-1]
                        _isOptional = True
                        parameters = (_idClass, _idProficiency, _isOptional)
                        cursor.execute(queryClassProficiences,parameters)

                for proficiency in c['proficiencies']:
                        _idProficiency = proficiency['url'].split("/")[-1]
                        _isOptional = False
                        parameters = (_idClass, _idProficiency, _isOptional)
                        cursor.execute(queryClassProficiences,parameters)

                #--------------saving throw-------------------------
                for savingThrow in c['saving_throws']:
                        _idAbility = savingThrow['url'].split("/")[-1]
                        parameters = (_idClass, _idAbility)
                        cursor.execute(queryClassSavingThrows,parameters)

                #-----------starting equipment-------------------------
                #TODO dodać parsowanie starting equipment z classes.json

                #-----------subclasses--------------------------
                if('subclasses' in c):
                    for subclass in c['subclasses']:
                            _className = subclass['name']
                            parameters = (_idClass, _className)
                            cursor.execute(queryClassSubclasses,parameters)

if __name__ == "__main__":
    generate()
    saveDB()
    closeDB()