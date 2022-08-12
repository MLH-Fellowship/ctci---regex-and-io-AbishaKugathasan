import re 
import os

#convert the python file into a string 
text = open("vowel.txt")
    
# Write the solution for "Filter Vowels".
#Count the number of vowels 

#find the vowels by using regex 
vowels = (a|e|i|o|u)

#count the vowels by storing it in an array 
number_of_vowels = len(re.findall(vowels, text))

#Change the name of the file to vowels-number.txt
os.rename("vowel.txt", "vowels-"+number_of_vowels"+".txt"
