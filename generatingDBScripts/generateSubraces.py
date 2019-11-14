from connectDB import db, cursor, saveDB, closeDB
import json

def generate():
    with open("data/5e-SRD-Subraces.json", "r") as read_file:
        querySubraces = "INSERT INTO subraces VALUES (NULL, %s, %s, %s, %s);"
        querySubraceTraits = "INSERT INTO subracetraits VALUES (NULL, %s, %s, %s);"
        querySubraceAbilities = "INSERT INTO subraceabilities VALUES (NULL, %s, %s, %s, %s);"
        querySubraceStartingProficiences = "INSERT INTO subracestartingproficiences VALUES (NULL, %s, %s, %s);"
        queryRaceSubraces = "INSERT INTO racesubraces VALUES (NULL, %s, %s);"
        data = json.load(read_file)
        for subrace in data:

#           SUBRACES

            parameters = []
            _idSubrace = subrace["index"]
            parameters.append(_idSubrace)   
            parameters.append(subrace["desc"])
            if "choose" in subrace["racial_trait_options"]:
                parameters.append(subrace["racial_trait_options"]["choose"])
            else:
                parameters.append(0)
            if "choose" in subrace["starting_proficiency_options"]:
                parameters.append(subrace["starting_proficiency_options"]["choose"])
            else:
                parameters.append(0)
            cursor.execute(querySubraces,parameters)

#           RACIAL TRAITS

            for trait in subrace["racial_traits"]:
                parameters = []
                parameters.append(False)
                parameters.append(_idSubrace)
                _idTrait = trait["url"].split("/")[-1]
                parameters.append(_idTrait)
                cursor.execute(querySubraceTraits,parameters)

            if "from" in subrace["racial_trait_options"]:
                for trait in subrace["racial_trait_options"]["from"]:
                    parameters = []
                    parameters.append(True)
                    parameters.append(_idSubrace)
                    _idTrait = trait["url"].split("/")[-1]
                    parameters.append(_idTrait)
                    cursor.execute(querySubraceTraits,parameters)
            
#           ABILITY BONUSES

            for ability in subrace["ability_bonuses"]:
                parameters = []
                parameters.append(ability["bonus"])
                parameters.append(False)
                parameters.append(_idSubrace)
                _idAbility = ability["url"].split("/")[-1]
                parameters.append(_idAbility)
                cursor.execute(querySubraceAbilities,parameters)

            if "from" in subrace["ability_bonus_options"]:
                for ability in subrace["ability_bonus_options"]["from"]:
                    parameters = []
                    parameters.append(ability["bonus"])
                    parameters.append(True)
                    parameters.append(_idSubrace)
                    _idAbility = ability["url"].split("/")[-1]
                    parameters.append(_idAbility)
                    cursor.execute(querySubraceAbilities,parameters)

    #       STARTING PROFICIENCIES

            for proficiency in subrace["starting_proficiencies"]:
                parameters = []
                parameters.append(False)
                _idProficiency = proficiency["url"].split("/")[-1]
                parameters.append(_idProficiency)
                parameters.append(_idSubrace)
                cursor.execute(querySubraceStartingProficiences,parameters)

            if "from" in subrace["starting_proficiency_options"]:
                for proficiency in subrace["starting_proficiency_options"]["from"]:
                    parameters = []
                    parameters.append(True)
                    _idProficiency = proficiency["url"].split("/")[-1]
                    parameters.append(_idProficiency)
                    parameters.append(_idSubrace)
                    cursor.execute(querySubraceStartingProficiences,parameters)

#           RACE SUBRACES

            parameters = []
            _idRace = subrace["race"]["url"].split("/")[-1]
            parameters.append(_idRace)
            parameters.append(_idSubrace)
            cursor.execute(queryRaceSubraces,parameters)       
                


if __name__ == "__main__":
    generate()
    saveDB()
    closeDB()