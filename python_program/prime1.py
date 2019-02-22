num=int(input("Enter the Number ")) #9
for i in range(2,num+1):  #(2,10)	
	if(num%i==0):	#9%3==0
		break
if(i==num and num>=2):
	print("Prime")
else:
	print("Not Prime")

