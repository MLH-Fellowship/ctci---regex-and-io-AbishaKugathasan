import re 
from string import * 

print("opening file")
pattern = "\s"
count = 0

with open ('meta.txt','r') as f:
  context = f.read()
  length = len(context)
  number_of_files = length/200
  result = re.split(pattern, context, 10)
  #print(result[0])

for x in result: 
  count = count+1
  string = str(count)
  f = open("meta-"+string+".txt", "a")
  result_array = result[count-1]
  result_string = str(result_array)
  f.write(result_string)
  f.close()
  #print(result)
