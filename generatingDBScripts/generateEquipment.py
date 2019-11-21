from connectDB import db, cursor, saveDB, closeDB
import json



def generate():
    with open("data/5e-SRD-Equipment.json", "r") as read_file:
        query = "INSERT INTO  VALUES (%s, NULL,%s,%s);"
        data = json.load(read_file)
        eqCategories = []
        for eq in data:
            category = eq['equipment_category']
            if(category not in eqCategories):
                eqCategories.append(category)

        allFields = []
        categoryFields = []

        for category in eqCategories:
            fields = []
            for eq in data:
                if(eq['equipment_category']!=category):
                    continue
                for field in eq:
                    if(field not in fields):
                        fields.append(field)
                    if(field not in allFields):
                        allFields.append(field)
            categoryFields.append(fields)
            print(category, fields)

        uncommonFields = []
        for field in allFields:
            for category in categoryFields:
                if(field not in category):
                    uncommonFields.append(field)
                    break
            
                    
                
                
        print("\n\nuncommon categories: ")
        print(uncommonFields)

        for field in allFields:
            if field not in uncommonFields:
                print(field)
            # _api = skill["ability_score"]["url"].split("/")[-1]
            #parameters = ()
           # cursor.execute(query, parameters)
            
            
                
        

if __name__ == "__main__":
    generate()
    saveDB()
    closeDB()
