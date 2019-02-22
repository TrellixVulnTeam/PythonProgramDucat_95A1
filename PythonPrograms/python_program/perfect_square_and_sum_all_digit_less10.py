#102. Program to Find all Numbers in a Range which are Perfect Squares and Sum of all Digits in the Number is Less than 10

list=[]
n= int(input("enter the lower limit:"))
m= int(input("enter the upper limit:"))
i=1
while i < m+1:      # i is greater than upper limit +1 times .
      n=i*i               # find the perfect square in lower limit to upper limit in range.
      i = i + 1
      print(n)
      list.append(n)
print(list)
