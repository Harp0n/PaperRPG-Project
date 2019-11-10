import json

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
            
        
def retriveDamage(spellDescription):
    words = spellDescription.split()
    for word in words:
        if len(word) >= 3 and len(word) <= 5:
            if hasNumbers(word):
                if word.find("d") == 1:
                    return word
def retriveDmgType(spellDescription, dmgTypes):
    spellDesc = spellDescription.split()
    for desc in spellDesc:
        for dmgType in dmgTypes:
            if dmgType.lower() in spellDesc:
                return dmgType
        
    

file = open("Spells.json", "r") 

parseJson = json.load(file)

listOfDmgSpells = []

fileDmgTypes = open("5e-SRD-Damage-Types.json", "r")
parsedDMGtypes = json.load(fileDmgTypes)

stringTest = "4d4 damage acid"

print("acid" in stringTest.split())

dmgTypes = []
      
for dmgType in parsedDMGtypes:
    dmgTypes.append(dmgType["name"])
    ##print(dmgType["name"])


for spell in parseJson:
    description = spell["desc"]
    for desc in description:
        dmg = retriveDamage(desc)
        dmgType = retriveDmgType(desc, dmgTypes)

    if dmg != None and dmgType != None:
        helpString = (spell["name"] + " " + dmg + " DMG TYPE: " + dmgType)
        listOfDmgSpells.append(helpString)

    elif dmg != None:
        helpString = (spell["name"] + " " + dmg)
        listOfDmgSpells.append(helpString)
    else:
        helpString = (spell["name"] + " no dmg")
        listOfDmgSpells.append(helpString)
        

        
for spell in listOfDmgSpells:
    print(spell)



##class Spell():
##    def __init__(name, damage):
##        self.name = name
##       self.damage = damage





