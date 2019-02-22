n= int(input("enter the no:"))
temp = n
sum=0
while n>0:
     rem = n%10
     sum = sum*10+rem
     n=n//10
print(sum)
if temp==sum:
    print("its number is plaindrome.")
else:
    print("its number is not plaindrome.")


# run-> cmd-> cd desktop-> ducatwork-> filename-> python filename.py    (enter key press)....
