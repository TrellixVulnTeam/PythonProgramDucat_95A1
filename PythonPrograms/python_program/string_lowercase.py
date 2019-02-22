#66.  Count Number of Lowercase  and upper case Characters in a String & both lower and upper in one string find.  ??


string= input("Enter string:")
count=0
for i in string:
      if(i.islower()):       # only count for lower case charters .
            count=count+1
print("The number of lowercase characters :",count)
