import json
import difflib  #std python lib
from difflib import get_close_matches

data = json.load(open("APP1/data.json"))  #to load the file consisting of all the words and their meanings

#function 
def fetch(w):
    w = w.lower()  #converts the obtained word into lower case
    if w in data:  #checks if the input word is present in the json file
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]    
    elif len(get_close_matches(w, data.keys()))>0:   
        yn = input("Did you mean %s instead? \n Enter Y for yes, N for no \n" % get_close_matches(w, data.keys())[0])    #checks for the closest match to the input word
        if yn =="Y" or "y":
            return data[get_close_matches(w, data.keys())[0]]   
    else:
        return "Word not found"    

#user input
word = input("Enter a word: ")

output = fetch(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)        

