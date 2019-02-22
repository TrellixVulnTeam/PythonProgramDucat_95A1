#  count the string any value find the index of char ...???
# chr index in any user print string all index can print in any 

a="Python includes following functions that perform mathematical calculations and all these functions cannot be used directly and for that we need to import the math function in it"
b= len(a)
print(b)
for i in range(b):
#print(i)/ # print(a[i],i)   ===>>>  print all char and char index both print ..
	if a[i]=="o":
		print(a[i],i)    # print all 'o' in print string and index also print. 