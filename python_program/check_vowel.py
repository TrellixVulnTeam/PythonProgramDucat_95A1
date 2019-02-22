# Python Program - Check Vowel or Not


ch = input("Enter only character: ")

if(ch=='a' or ch=='A' or ch=='e' or ch=='E' or ch=='i' or ch=='I' or ch=='o' or ch=='O' or ch=='u' or ch=='U'):
    	    print(ch, "is a vowel.")
else:
    print(ch, "is not a vowel.")
	
	
'''
output ==

ch = i
is a vowel.

Enter only character: ram
ram is not a vowel.
'''


str = input("Enter any string : ")
for ch in str:
	if(ch=='a' or ch=='A' or ch=='e' or ch=='E' or ch=='i' or ch=='I' or ch=='o' or ch=='O' or ch=='u' or ch=='U'):
		print(ch, "is a vowel.")
	else:
		print( ch,"is not a vowel.")
		
		
'''
output ==

Enter any string : ramvinay
r is not a vowel.
a is a vowel.
m is not a vowel.
v is not a vowel.
i is a vowel.
n is not a vowel.
a is a vowel.
y is not a vowel.

'''