# import json
import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()

def getDef(word):
    word = word.lower()
    query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
    print(type(query))
    results = cursor.fetchall()

    if len(results) > 0:
        return results
    else:
        return "Word not found. Check your input."

searchDef = input("What word would you like to define: ")
definition = getDef(searchDef)

if type(definition) is list:
    for line in definition:
        print(line[0])
else:
    print(definition)