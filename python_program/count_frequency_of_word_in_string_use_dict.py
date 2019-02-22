#69.   Count the Frequency of Words Appearing in a String Using a Dictionary.


str = input("Enter string:")
l=[]
l= str.split()
word =[l.count(p) for p in l]
print(dict(zip(l,word)))