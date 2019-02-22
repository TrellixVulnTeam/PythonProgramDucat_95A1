# Python Make Simple Calculator  ????

print("Enter any two number: ")
num1 = input();
num2 = input();

ch = input("Enter operator (+,-,*,/,//,%,**,root): ")
if ch == '+':
    res = int(num1) + int(num2);
    print(num1, "+", num2, "=", res)
elif ch == '-':
    res = int(num1) - int(num2);
    print(num1, "-", num2, "=", res)
elif ch == '*':
    res = int(num1) * int(num2);
    print(num1, "*", num2, "=", res)
elif ch == '/':
    res = int(num1) / int(num2);
    print(num1, "/", num2, "=", res)
elif ch == '//':
    res = int(num1) // int(num2);
    print(num1, "//", num2, "=", res)
elif ch == '%':
    res = int(num1) % int(num2);
    print(num1, "%", num2, "=", res)
elif ch == '**':
    res = int(num1) ** int(num2);
    print(num1, "**", num2, "=", res)
elif ch == 'root':
	res = (int(num1)) ** (1/2)
	res1 = (int(num2)) ** (1/2)
	print(num1, "root" "=", res)
	print(num2, "root" "=", res1)
else:
    print("Strange input..exiting..")
	
	
'''
output == 
calcultor basic : 
Enter any two number:
45
96
Enter operator (+,-,*,/,//,%,**,root): root
45 root= 6.708203932499369
96 root= 9.797958971132712

'''