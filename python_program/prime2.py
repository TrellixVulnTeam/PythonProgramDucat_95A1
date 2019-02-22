num=int(input("Enter the Number ")) 
f=0
for i in range(2,(num//2)+1): #7427466391 7(2,4)
	if(num%i==0): #7%3==0
		f=1
		break
if(f==0 and num>=2):
	print("Prime")
else:
	print("Not Prime")

