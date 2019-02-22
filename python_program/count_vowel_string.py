# Python Program to Count the Number of Each Vowel  ????
# Program to count the number of each vowel in a string
# string of vowels


vowels = 'aeiou'

# change this value for a different result

str = 'Hello, have you tried our turorial section yet?'

# uncomment to take input from the user

# str = input("Enter a string: ")

# make it suitable for caseless comparisions

str = str.casefold()

# make a dictionary with each vowel a key and value 0

count = {}.fromkeys(vowels,0)

# count the vowels

for char in str:
   if char in count:
       count[char] += 1

print("total vowel in given string : ==== ",count)


'''
output == 

total vowel in given string  : ====   {'a': 2, 'e': 5, 'i': 3, 'o': 5, 'u': 3}

'''