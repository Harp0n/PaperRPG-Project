from connectDB import db, cursor, saveDB, closeDB
import json

def generate():
    with open("data/5e-SRD-Races.json", "r") as read_file:
            queryRaces = "INSERT INTO races VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s);"
            queryRaceAbilities = "INSERT INTO raceAbilities VALUES (NULL,%s,%s,%s,%s);"
            queryRaceStartingProficiency = "INSERT INTO starting_proficiences VALUES (NULL,%s,%s,%s);"
            data = json.load(read_file)
            for race in data:
                _idRace = race['index']
                _name = race['name']
                _speed = race['speed']
                _alignment = race['alignment']
                _age = race['age']
                _size = race['size']
                _size_description = race['size_description']
                if "choose" in  race['ability_bonus_options']:
                    _ability_bonus_options_count = race['ability_bonus_options']['choose']
                else:
                    _ability_bonus_options_count = 0
                if "choose" in  race['starting_proficiency_options']:
                    _starting_proficiences_options_count = race['starting_proficiency_options']['choose']
                else:
                    _starting_proficiences_options_count = 0
                parameters = (_name, _speed, _alignment, _age, _size, _size_description, _ability_bonus_options_count, _starting_proficiences_options_count)
                cursor.execute(queryRaces,parameters)
                
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