#80.     program  Detect if Two Strings are Anagrams .>>
# strings are anagrams - the value of sort form string in order and same word in pattern word
   # in incresd order the same number of any word so it is called anagram no.

n= input("enter the value:")
m= input("enter the value:")
if ((sorted(n)== (sorted(m)))):           # the value of sort used in strings.>>
    print("the value of string are anagram.")
else:
    print("the value of string are not anagram.")