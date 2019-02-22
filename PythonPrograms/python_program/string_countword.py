# counter of the condition given count the char in any sentense ...??


a= "hello python"
b= "– They are bunch of characters. In other words they are identified as contiguous(IN SEQUENCE) set of characters. Subset of strings can be taken using slice operator "
c=0
for x in a:
	if (x=="l"):
		c=c+1
print("total char count ",c)          ## output == 2
c1=0
for y in b:
	if (y=="e"):
		c1=c1+1
print("total chr count : ",c1)         ## output == 15