#119.   New String Made of the First 2 and Last 2 characters From a Given String .??

string= input("Enter string:")
count=0
for i in string:
      count=count+1
new=string[0:2]+string[count-2:count]       # two given string only add charter first two and last two charter.
print("Newly formed string is:",new)