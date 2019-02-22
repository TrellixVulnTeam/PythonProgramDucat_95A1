#71.  count the vowel & consonents number of input any strings input by user.??


string = input("enter the string name:")
vowels =0
consonents = 0
for i in string:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels = vowels+1       # count vowels.
    else:
        consonents= consonents+1
print("no of vowel in string :",vowels)
print("no of consonent in string :",consonents)
