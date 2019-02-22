#153.     Take in Two Strings and Display the Larger String without Using Built-in Functions .??

string1= input("Enter first string:")
string2= input("Enter second string:")
count1=0
count2=0
for i in string1:
      count1=count1+1
print("length of string1:",count1)
for j in string2:
      count2=count2+1
print("length of string2:",count2)
if(count1<count2):
      print("Larger string is:",string2)
elif(count1==count2):
      print("Both strings are equal.")
else:
      print("Larger string is:",string1)