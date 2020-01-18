import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def getDef(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff=0.9)) > 0:
        con = input("Did you mean %s?[y/n] " % get_close_matches(word, data.keys(), cutoff=0.8)[0])
        if con == 'y':
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        else:
            return "Word not found. Goodbye." 
    elif len(get_close_matches(word.title(), data.keys(), cutoff=0.8)) > 0:
        con = input("Did you mean %s?[y/n] " % get_close_matches(word.title(), data.keys(), cutoff=0.8)[0])
        if con == 'y':
            return data[get_close_matches(word.title(), data.keys(), cutoff=0.8)[0]]
        else:
            return "Word not found. Goodbye." 
    else:
        return "Word not found. Check your input."

searchDef = input("What word would you like to define: ")
definition = getDef(searchDef)

if type(definition) is list:
    for line in definition:
        print(line)
else:
    print(definition)