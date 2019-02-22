#72. Count the Number of Vowels Present in a String using Sets. ???

n = input("enter the string:")
vowel = 0
for x in n:  # x in only string value.
     if (
             x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U'):  # condition of vowel.
         vowel = vowel + 1
 print(vowel)

# another mathod to print string and count vowels :?

s = input("Enter string:")
count = 0
vowels = set("aeiou")  # vowel difine in set sepratly the vowels part. ??
for x in s:
     if x in vowels:
         # count += 1
         count = count + 1
print("Count of the vowels is:", count)
