# Python Program to Find the Factorial of a Number  ????

n= int(input("enter the no find fact. "))
# i=1         (no used in the program i=1  , because the while n>i: )
fact=1
# while n>i:
while n:
	fact= fact*n
	n=n-1
print("fact of given number == ",fact)