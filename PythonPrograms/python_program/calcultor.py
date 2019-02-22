a= int(input("enter the first number:"))
b= int(input("enter the second number:"))
print("+ for add. ")
print("- for sub. ")
print("* for mul. ")
print("/ for div. ")
c= input("enter the choice:")
if c=="+":
	print(a,"+",b,"=",a+b)
elif c=="-":
	print(a,"-",b,"=",a-b)
elif c=="*":
	print(a,"*",b,"=",a*b)
elif c=="/":
	print(a,"/",b,"=",a/b)
else:
	print("wrong input.")