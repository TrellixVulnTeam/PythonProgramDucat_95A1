#138.   Reverse a String Using Recursion . ??

def reverse(str):
    reversed_str= ""
    for i in str:
        reversed_str = i+reversed_str
    print("reverse of string:",reversed_str)
str= input("enter the string:")
print("enter the string :",str)
reverse(str)