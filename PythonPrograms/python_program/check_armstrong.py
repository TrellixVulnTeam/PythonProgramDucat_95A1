# check the armstrong number or not input by user ..???

n= int(input("enter the no:"))
temp = n
sum=0
while n>0:
     rem = n%10
     sum = sum +rem**3
     n=n//10
print(sum)
if temp==sum:
    print("its number is armstrong.")
else:
    print("its number is not armstrong.")


# run-> cmd-> cd desktop-> ducatwork-> filename-> python filename.py    (enter key press)....