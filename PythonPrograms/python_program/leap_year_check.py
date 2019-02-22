# Python Program to Check Leap Year ????

y= int(input("enter the year no. "))
if ((y%4==0 and y%100!=0) or y%400==0):
	print("year is leap year.")
else:
	print("year is non leap year.")