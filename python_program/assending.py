a= int(input("enter the no :"))
b= int(input("enter the no :"))
c= int(input("enter the no :"))
if a>b and b>c:
	print("desending order :",a,b,)
	print("assending order :",c,b,a)
	
elif b>c and c>a:
	print("desending order :",b,c,a)
	print("assending order :",a,c,b)
	
else:
	print("desending order :",c,a,b)
	print("assending order :",b,a,c)
    