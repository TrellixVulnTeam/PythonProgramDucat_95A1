a="the world is the india most devloped country."
print(a.index("most"))
b= a.split()
sum=0
k=1
for x in range(len(b)):
	if (b[x]=="most"):
		
		
	k=k+1
	sum=sum+len(b[x])+k
	print(sum)
print(sum+len(b)-1)
print(len(a))
print(a.find("most"))
