# Write the solution for "New Emails".
import rm
#Regex to find the '@gmail.com' part, so I can change it to mlh.io - only gets the valid emails as said in the prompt (@([a-zA-z])+\.com) 
replace (@([a-zA-z])+\.com, @mlh.io)
