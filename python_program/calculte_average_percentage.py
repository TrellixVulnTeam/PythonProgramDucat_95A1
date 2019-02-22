# Python Calculate Average Percentage  ????

n = int(input("enter the value of term : "))
t_mark = n * 100
sum = 0
for i in range(1,n+1):
	m = int(input("marks: "))
	sum = sum + m
average = (sum)/n 
print("total average of value of n term : ===",average)
percent = (sum * 100)/(t_mark)
print("total percentage : ",percent,"%")

'''
output ===

enter the value of term : 5
marks: 96
marks: 87
marks: 78
marks: 58
marks: 98
total average of value of n term : === 83.4
total percentage :  83.4 %

'''