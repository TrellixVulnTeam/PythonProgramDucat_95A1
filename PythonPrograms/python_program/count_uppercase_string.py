#67. count number of uppercase charters in strings. ??

string= input("Enter string:")
count=0
for i in string:
      if(i.isupper()):       # only count for upper case charters .
            count=count+1
print("The number of uppercase characters :",count)