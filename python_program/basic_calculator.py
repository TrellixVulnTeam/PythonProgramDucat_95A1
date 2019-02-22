# Python Program to Make a Simple Calculator  ????

a= float(input("enter the number: "))
b= float(input("enter the number: "))
print("choice 1 for addition ")
print("choice 2 for substract ")
print("choice 3 for multipication ")
print("choice 4 for divisable ")
print("choice 5 for floar divisable ")
choice = int(input("enter the choice for user : "))
if choice == 1:
	print(a,"+",b,"=",a+b)
elif choice == 2:
	print(a,"-",b,"=",a-b)
elif choice == 3:
	print(a,"*",b,"=",a*b)
elif choice == 4:
	print(a,"/",b,"=",a/b)
elif choice ==5:
	print(a,"//",b,"=",a//b)
else:
	print("invalid input of users choice . ")