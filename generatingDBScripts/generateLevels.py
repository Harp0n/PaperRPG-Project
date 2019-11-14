from connectDB import db, cursor, saveDB, closeDB
import json

def generate():
    with open("data/5e-SRD-Levels.json", "r") as read_file:
            queryFeatures = "INSERT INTO levels VALUES (%s,NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            queryLevelFeatures =  "INSERT INTO levelfeatures VALUES (NULL,%s,%s);"

            data = json.load(read_file)
            for level in data:
                _className = level['class']['name']
                if ('level' in level):
                    _level = level['level']
                else:
                    _level = 0
                if('ability_score_bonuses' in level):
                     _abilityScoreBonuses = level['ability_score_bonuses']
                else:
                    _abilityScoreBonuses = 0
                if('prof_bonus' in level):
                    _profBonus = level['prof_bonus']
                else:
                    _profBonus = 0
                if('spellcasting' in level):
                    sc = level['spellcasting']
                    if('cantrips_known' in sc):
                        cantrips_known = sc['cantrips_known']
                    else:
                        cantrips_known = 0

                    if('spells_known' in sc):
                        spells_known = sc['spells_known']
                    else:
                        spells_known = 0

                    if('spell_slots_level_1' in sc):
                        spell_slots_level_1 = sc['spell_slots_level_1']
                    else:
                        spell_slots_level_1 = 0

                    if('spell_slots_level_2' in sc):
                        spell_slots_level_2 = sc['spell_slots_level_2']
                    else:
                        spell_slots_level_2 = 0

                    if('spell_slots_level_3' in sc):
                        spell_slots_level_3 = sc['spell_slots_level_3']
                    else:
                        spell_slots_level_3 = 0

                    if('spell_slots_level_3' in sc):
                        spell_slots_level_3 = sc['spell_slots_level_3']
                    else:
                        spell_slots_level_3 = 0

                    if('spell_slots_level_4' in sc):
                        spell_slots_level_4 = sc['spell_slots_level_4']
                    else:
                        spell_slots_level_4 = 0

                    if('spell_slots_level_5' in sc):
                        spell_slots_level_5 = sc['spell_slots_level_5']
                    else:
                        spell_slots_level_5 = 0

                    if('spell_slots_level_6' in sc):
                        spell_slots_level_6 = sc['spell_slots_level_6']
                    else:
                        spell_slots_level_6 = 0

                    if('spell_slots_level_7' in sc):
                        spell_slots_level_7 = sc['spell_slots_level_7']
                    else:
                        spell_slots_level_7 = 0

                    if('spell_slots_level_8' in sc):
                        spell_slots_level_8 = sc['spell_slots_level_8']
                    else:
                        spell_slots_level_8 = 0

                    if('spell_slots_level_9' in sc):
                        spell_slots_level_9 = sc['spell_slots_level_9'] 
                    else:
                        spell_slots_level_9 = 0
                    parameters = (_className, _level, _abilityScoreBonuses, _profBonus, cantrips_known, spells_known, spell_slots_level_1, spell_slots_level_2,
                                    spell_slots_level_3, spell_slots_level_4, spell_slots_level_5, spell_slots_level_6, spell_slots_level_7, spell_slots_level_8,
                                    spell_slots_level_9)
                else:
                    parameters =  (_className, _level, _abilityScoreBonuses, _profBonus, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                cursor.execute(queryFeatures,parameters)

                for feature in level['features']:
                    _idFeature = feature['url'].split("/")[-1]
                    parameters = (_className, _idFeature)
                    cursor.execute(queryLevelFeatures, parameters) 
if __name__ == "__main__":
    generate()
    saveDB()
    closeDB()