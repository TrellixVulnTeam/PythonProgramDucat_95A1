#31.  Form an Integer that has the Number of Digits at Ten's Place and the Least Significant Digit of the Entered Integer at One's Place ..??



n=int(input("enter the no :"))
temp=n
count=0
while n>0:
    digit=n%10
    count=count+1
    n = n // 10
# print(count)
rem= temp%10
T = (count*10) + rem

print("replace the tenth place to count no: =",T)


'''
output ==
# total count digit in user input is 3 , and last(unit) digit is 9 , then replace the tenth place in count of digit and last are same in user values
   so    659  is digit = 3 and ones place = 9    =====>>>>>    output  ===  659  (enter the no by user)    *****   result == 39 .

enter the no :659
replace the tenth place to count no: = 39

'''





