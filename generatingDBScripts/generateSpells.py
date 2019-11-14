from connectDB import db, cursor, saveDB, closeDB
import json


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
    
def diceFromDesc(description):
    words = description.split()
    for word in words:
        if len(word) >= 1 and len(word) <= 5:
            if hasNumbers(word):
                if word.find("d") == 1:
                    return word

def retriveDmgType(spellDescription, dmgTypes):
    spellDesc = spellDescription.split()
    for desc in spellDesc:
        for dmgType in dmgTypes:
            if dmgType.lower() in spellDesc:
                return dmgType


def generate():
    with open("data/5e-SRD-Spells.json", "r") as read_file:
            querySpells = "INSERT INTO spells VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            querySpellsSubclasses = "INSERT INTO spellsubclasses VALUES (NULL,%s,%s);"
            querySpellClasses = "INSERT INTO spellclasses VALUES (NULL,%s,%s);"
            data = json.load(read_file)
            for spell in data:
                ## WITHOUT TABLES
                _idSpell = spell['index']
                _name = spell['name']
                _page = spell['page']
                _ritual = spell['ritual']
                _duration = spell['duration']
                _concentration = spell['concentration']
                if "material" in spell:
                    _material = spell['material']
                else:
                    _material = ""
                _castingTime = spell['casting_time']
                _lvl = spell['level']
                _range = spell['range']
                # WITH TABLES
                fullDescription = ""
                diceFromDescription = ""
                for desc in spell['desc']:
                    fullDescription += desc
                _fullDesc = fullDescription
                _diceFromDescription = diceFromDesc(fullDescription)

                fileDmgTypes = open("data//5e-SRD-Damage-Types.json", "r")
                parsedDMGtypes = json.load(fileDmgTypes)
                dmgTypes = ["heal", "healing", "healed", "regains"]
                for dmgType in parsedDMGtypes:
                    dmgTypeLowerCase = dmgType["name"]
                    dmgTypes.append(dmgTypeLowerCase.lower())
                _dmgType = retriveDmgType(fullDescription, dmgTypes)
##                if _diceFromDescription != None: 
##                    print(_name + " : " + _diceFromDescription)
##                if _diceFromDescription != None and _dmgType != None:
##                    print(_name + " : " + _diceFromDescription + " : " + _dmgType)
                _higherLvL = ""
                if "higher_level" in spell:
                    for desc in spell['higher_level']:
                        _higherLvL += desc
                
                    
                _components = ""
                for comp in spell["components"]:
                    _components += comp

                _idSchool = spell["school"]["url"].split('/')[-1]

                for subclass in spell["subclasses"]:
                    _idSubclass = subclass["url"].split('/')[-1]
                    print(_idSubclass)
                    parameter = ( _idSpell, _idSubclass)
                    cursor.execute(querySpellsSubclasses, parameter)

                for classs in spell["classes"]:
                    _idClass = classs["url"].split('/')[-1]
                    parameter = (_idSpell, _idClass)
                    cursor.execute(querySpellClasses, parameter)

                parameter = (_name, _fullDesc, _diceFromDescription, _dmgType,
                             _higherLvL, _page, _range, _components, _material,
                             _ritual, _duration, _concentration, _castingTime,
                             _lvl, _idSchool)

                cursor.execute(querySpells, parameter)

if __name__ == "__main__":
    generate()
    saveDB()
    closeDB()
