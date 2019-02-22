# Python Program - Addition Subtraction Multiplication Division


print("Enter any two number: ")
num1 = input();
num2 = input();

ch = input("Enter operator (+,-,*,/): ")
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
else:
    print("Strange input..exiting..")
	
	
'''
output ==

Enter any two number:
89
96
Enter operator (+,-,*,/): +
89 + 96 = 185

Enter any two number:
25
978
Enter operator (+,-,*,/): 3
Strange input..exiting..
'''