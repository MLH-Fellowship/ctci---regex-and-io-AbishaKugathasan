# Write the solution for "Longest Word".
# Write the solution for "Split the files".
#Exercise 2 - Longest Words 

#find the largest words by looping through the file 
` #set the longest word to be 0 
  length_of_longest_word = 0
  #regex part of it - gets the word 
  string = /\w+
  word_array = str.match(string)

#find the longest length of the word by going through the array 
  for (i =0; i < word_array.length(); i++)
    let length_of_current_string = str.len(word_array[i])
    if (length_of_current_string > length_of_longest_word):
      length_of_longest_word = length_of_current_string
    else: 
      continue
  
#Now, that I have the longest string, find all of those words and bold it 
  for (i=0; i < word_array.length(); i++)
    if (length_of_current_string == length_of_longest_word):
      #bold the word 
      print(word_array[i] + '\033[0m')
    else: 
      continue
