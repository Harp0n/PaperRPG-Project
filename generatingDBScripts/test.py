import mysql.connector
import json
import re

from connectDB import db, cursor, saveDB, closeDB
import createTables
import generateRaces, generateProficiencies, generateAbilityScores, generateEqTypes

    
def generateData():
    generateRaces.generate()
    generateProficiencies.generate()
    generateAbilityScores.generate()
    generateEqTypes.generate()
            
if __name__ == "__main__":
    createTables.create()
    generateData()

    saveDB()
    closeDB()
