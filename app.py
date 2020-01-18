import json

data = json.load(open("data.json"))

def getDef(word):
    if word in data:
        return data[word]
    else:
        print("Word not found")
        exit()

searchDef = input("What word would you like to define: ")
definition = getDef(searchDef)

print(definition)