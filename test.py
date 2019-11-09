import mysql.connector
import json
import re


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="haslo1",
  database='RPG',
  auth_plugin='mysql_native_password'
)
cursor = mydb.cursor()

addLanguageTable = """CREATE TABLE IF NOT EXISTS `languages` (
	`id` int(10) NOT NULL AUTO_INCREMENT,
	`name` varchar(255),
	`type` varchar(255),
	`script` varchar(255),
	PRIMARY KEY( `id` )
);"""

def addTables():
    with open("tables.txt", "r") as read_file:
        data = read_file.read()
        
        for query in data.split(';'):
            if(query!=''):
                final_query = query+';'

                lines=final_query.split('\n')
                for line in lines:
                    result = re.search("CREATE TABLE `(.*)`",line)
                    if(result != None):
                        tableName = result.group(1)
                        dropQuery = "DROP TABLE IF EXISTS " + tableName + ";"
                        cursor.execute(dropQuery)
                
                cursor.execute(final_query)

    
def generateData():
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
    with open("data/5e-SRD-Proficiencies.json", "r") as read_file:
        
        query = "INSERT INTO proficiences VALUES (NULL,%s,%s);"
        data = json.load(read_file)
        for proficiency in data:
            _type = proficiency['type']
            _name = proficiency['name']
            parameters = (_type, _name)
            cursor.execute(query,parameters)
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
            
addTables()
generateData()    



##add_language = "INSERT INTO languages VALUES (NULL,%s,%s,%s);"

##with open("data/5e-SRD-Languages.json", "r") as read_file:
##    languageArray = json.load(read_file)
##    for language in languageArray:
##        _name = language['name']
##        _type = language['type']
##        _script = language['script']
##        cursor.execute(add_language, (_name, _type, _script))
##        



##command = ("""INSERT INTO languages VALUES (NULL, 'Common', 'Standard', 'Common');""")
##cursor.execute(command)





mydb.commit()

cursor.close()
mydb.close()
