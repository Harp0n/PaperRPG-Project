from connectDB import db, cursor, saveDB, closeDB
import json

def generate():
    with open("data/5e-SRD-Spellcasting.json", "r") as read_file:
        query = "INSERT INTO spellcasting VALUES (NULL,%s,%s,%s,%s);"
        data = json.load(read_file)
        for spellcasting in data:
            if('level' in spellcasting):
                _level = spellcasting['level']
            else:
                _level = 0
            _spellcastingAbilityID = spellcasting['spellcasting_ability']['url'].split("/")[-1]
            _infos = ""
            for info in spellcasting['info']:
                _infos += "<" + info['name'] +">\n"
                for line in info['desc']:
                    _infos += (line + "\n")

            _idClass = spellcasting['class']['url'].split("/")[-1]
            parameters = (_level, _spellcastingAbilityID, _infos, _idClass)
            cursor.execute(query,parameters)

if __name__ == "__main__":
    generate()
    saveDB()
    closeDB()