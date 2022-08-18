import re
from string import *
print("opening file")

with open ('emails.txt', 'r') as f:
  context = f.read()
  print(re.sub("@([a-zA-z])+\.com", "mlh.io",context))
