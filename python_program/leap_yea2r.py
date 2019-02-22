year=int(input("Enter the Year "))
if(year%400==0):
	print(year," is leapyear")
elif(year%4==0 and year%100!=0):
	print(year," is leapyear")
else:
	print(year," is not a leapyear ")