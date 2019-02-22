c=0
for num in range(1,1000):
	f=0
	for i in range(2,int(num**.5)+1):#(2,3)
			if(num%i==0):
				f=1
				break
		if(f==0 and num>=2):
			print(num,"Prime")
			c+=1
print("Total Prime : ",c)		
	#7427466391