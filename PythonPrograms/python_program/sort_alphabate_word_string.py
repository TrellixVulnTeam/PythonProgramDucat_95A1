'''
# Python Program to Sort Words in Alphabetic Order ????
# Program to sort alphabetically the words form a string provided by the user
'''

str = "Hello this Is an Example With cased letters"
# str = input("Enter a string: ")

# breakdown the string into a list
words = str.split()

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)
   
'''

output == 

The sorted words are:
Example
Hello
Is
With
an
cased
letters
this

'''