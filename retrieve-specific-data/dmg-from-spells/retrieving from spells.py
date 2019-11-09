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


file = open("Spells.json", "r") 

parseJson = json.load(file)

listOfDmgSpells = []

for spell in parseJson:
    description = spell["desc"]
    for desc in description:
        dmg = retriveDamage(desc)

    if dmg != None:
        print(spell["name"] + " " + dmg)
        helpString = (spell["name"] + " " + dmg)
        listOfDmgSpells.append(helpString)
    else:
        print(spell["name"] + " no dmg")
        helpString = (spell["name"] + " no dmg")
        listOfDmgSpells.append(helpString)

        
print(len(listOfDmgSpells))



##class Spell():
##    def __init__(name, damage):
##        self.name = name
##       self.damage = damage





