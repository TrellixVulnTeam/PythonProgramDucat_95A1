# user input the value has printed the value form ...??


a=[[4,5,6],[4,8,9],[4,5,9],[5,2,3],[70,52,36]]
b=[]
for x in a:                       # x in a :   means x all value in a (like that ..   [4,5,6],[4,8,9].......)
	for i in x:                    # i in x :   means i all value in x (like that ..   4,5,6,4,8,9.......)
		if i==4:                  # condition check and print the value of i value is equal to condition print from value..  like[all 4 values (in present 4 all value printed)]
			b.append(x)
print(b)