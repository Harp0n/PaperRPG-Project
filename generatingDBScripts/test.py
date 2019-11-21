import mysql.connector
import json
import re

from connectDB import db, cursor, saveDB, closeDB
import createTables
import generateRaces, generateProficiencies, generateAbilityScores, generateEqCategories
import generateClasses,generateConditions,generateDamageTypes,generateFeatures
import generateLanguages,generateLevels,generateMagicSchools,generateProficiencies
import generateRaces,   generateSkills, generateSpellcasting,generateSpells
import generateSpells,generateSubclasses,generateSubraces,generateTraits

## Generujemy tutaj wszystkie tabelki bazy danych z skryptów
def generateData():
    generateRaces.generate()
    generateProficiencies.generate()
    generateAbilityScores.generate()
    generateEqCategories.generate()
    generateClasses.generate()
    generateConditions.generate()
    generateDamageTypes.generate()
    generateFeatures.generate()
    generateLanguages.generate()
    generateLevels.generate()
    generateMagicSchools.generate()
    generateProficiencies.generate()
    generateRaces.generate()
    generateSkills.generate()
    generateSpellcasting.generate()
    generateSpells.generate()
    generateSubclasses.generate()
    generateSubraces.generate()
    generateTraits.generate()
            
if __name__ == "__main__":
    createTables.create()
    generateData()

    saveDB()
    closeDB()
