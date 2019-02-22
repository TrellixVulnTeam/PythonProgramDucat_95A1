# break to continue value append to list searching...??


a=[]             
while True:
	b=[]      
	q=input("a: ")
	w=input("b: ")
	b.append(q)
	b.append(w)
	a.append(b)
	c= int(input("press 1 to break "))         # break to c==1 print(any value other print then list print that ....)
	if c == 1:          # if c==1 print the user then print the break of list element...
		break
print(a)
