# any string input by user two one reverse and another same string print ....??


str= input("enter the any string by users : ")
length=len(str)
print("orignal string is: ")
print(str)
s=""
for i in range(length-1,-1,-1):
	if (i==0 or str[i-1] ==" "):
		for j in range(i,length):
			if (str[j]==" "):
				break
			else:
				s = s+str[j]
		s=s+" "
print("string in reverse word by word: ")
print(s)