# string print reverse ...??

a= "The method strip returns copy of the string in which all chars have been stripped from the beginning and the end of the string default whitespace characters"
b=""
c=len(a)
for x in range(c):
	b=a[x]+b
print(b)