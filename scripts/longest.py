import re 
from string import * 

print("opening file")
pattern = "\w+"
regex = re.compile(pattern)

with open ('longest.txt','r') as f: 
  context = f.read()
  words_found = regex.findall(context)

if words_found:
    longest_word = max(words_found, key=lambda word: len(word))
    print('\033[1m' + longest_word)
