from connectDB import db, cursor, saveDB, closeDB
import json

def generate():
    with open("data/55e-SRD-Classes.json", "r") as read_file:
            queryClasses = "INSERT INTO classes VALUES (NULL,%s,%s,%s);"
            queryClassProficiences = "INSERT INTO classproficiencies VALUES (NULL,%s,%s,%s);"
            queryClassSavingThrows = "INSERT INTO classesclasssavingthrows VALUES (NULL,%s,%s);"
            data = json.load(read_file)
            for c in data:
                _idClass = c['index']
                _name = c['name']
                _hitDie = c['hit_die']
                if('choose' in c['proficiency_choices']):
                    _proficiencyChoicesCount = c['proficiency_choices']['choose']
                else:
                    _proficiencyChoicesCount = 0
                parameters = (_name, _hitDie, _proficiencyChoicesCount)
                cursor.execute(queryClasses, parameters)
                #------------proficiencies--------------
                if('from' in c['proficiency_choices']):
                    for proficiency in c['proficiency_choices']['from']:
                        _idProficiency = proficiency['url'].split("/")[-1]
                        _isOptional = True
                        parameters = (_idClass, _idProficiency, _isOptional)
                        cursor.execute(queryClassProficiences,parameters)

                for proficiency in c['proficiencies']:
                        _idProficiency = proficiency['url'].split("/")[-1]
                        _isOptional = False
                        parameters = (_idClass, _idProficiency, _isOptional)
                        cursor.execute(queryClassProficiences,parameters)
                #-----------saving throws--------------------------
                for savingThrow in c['saving_throws']:
                        _idAbility = savingThrow['url'].split("/")[-1]
                        parameters = (_idClass, _idAbility)
                        cursor.execute(queryClassSavingThrows,parameters)

                



            parameters = (_type, _name)
            cursor.execute(query,parameters)









                for ability_bonus in race['ability_bonuses']:
                    _bonus = ability_bonus['bonus']
                    _idAbility = ability_bonus['url'].split("/")[-1]
                    _isOptional = False
                    parameters = (_bonus, _idRace, _idAbility, _isOptional)
                    cursor.execute(queryRaceAbilities, parameters)

                if('from' in race['ability_bonus_options']):
                    for ability_bonus in race['ability_bonus_options']['from']:
                        _bonus = ability_bonus['bonus']
                        _idAbility = ability_bonus['url'].split("/")[-1]
                        _isOptional = True
                        parameters = (_bonus, _idRace, _idAbility, _isOptional)
                        cursor.execute(queryRaceAbilities, parameters)

                    
                for starting_proficiency in race['starting_proficiencies']:
                    _isOptional = False
                    _idProficiency = starting_proficiency['url'].split("/")[-1]
                    parameters = (_isOptional, _idRace, _idProficiency)
                    cursor.execute(queryRaceStartingProficiency, parameters)

                if('from' in race['starting_proficiency_options']):
                    for starting_proficiency in race['starting_proficiency_options']['from']:
                        _isOptional = True
                        _idProficiency = starting_proficiency['url'].split("/")[-1]
                        parameters = (_isOptional, _idRace, _idProficiency)
                        cursor.execute(queryRaceStartingProficiency, parameters)

if __name__ == "__main__":
    generate()
    saveDB()
    closeDB()