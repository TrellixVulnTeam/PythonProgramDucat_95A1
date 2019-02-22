# Python Program to Remove Punctuations From a String   ????

# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

str = "Hello!!!, he said ---and went."

# To take input from the user
# str = input("Enter a string: ")


# remove punctuation from the string

no_punct = ""

for char in str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string

print("remove all punctuation of string : ",no_punct)


'''
output == 
str = "Hello!!!, he said ---and went."
remove all punctuation of string :  Hello he said and went

'''

# *************************   Python Program to Remove Punctuations From a String   ????    ******************************  #

# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# To take input from the user

str = input("Enter a string: ")

# remove punctuation from the string

no_punct = ""

for char in str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string

print("remove all punctuation of string : ",no_punct)

'''
output == 

Enter a string: hello! ram din @ what?are U & say*
remove all punctuation of string :  hello ram din  whatare U  say

'''