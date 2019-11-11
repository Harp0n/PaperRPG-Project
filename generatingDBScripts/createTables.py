from connectDB import db, cursor, saveDB, closeDB
import re

def create():
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

if __name__ == "__main__":
    create()
    saveDB()
    closeDB()
