import json

data = json.load(open("data.json"))

def getDef(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "Word not found."

searchDef = input("What word would you like to define: ")
definition = getDef(searchDef)

print(definition)