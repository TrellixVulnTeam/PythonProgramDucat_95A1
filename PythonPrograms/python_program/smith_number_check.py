# smith number ==  likes 378 ==>>  3+7+8=18       prime factor of 378 ====>>  2*3*3*3*7  == 2+3+3+3+7 == 18
# 378 is smith number its digit sum to equal to its number factor sum is equal to number is called the smith number ...??


n= int(input("enter the no:"))
sum=0
t=n
while n!=0:
	rem= n%10
	sum=sum+rem
	n=n//10
print("digits sum enter the no :: == ",sum)
s=sum
sum1=0
arr = []
for i in range(2,t+1):
	flag = 0
	j = 2
	while j < i//2+1:
		if i % j == 0:
			flag = 1
			break
		j = j + 1
	if flag == 0:
		arr.append(i)

#print(arr)		
while t > 1:
	for k in range(0,len(arr)):
		if t % arr[k] == 0:
			print(arr[k],end='*')
			sum1 = sum1 + arr[k]
			t = t // arr[k]
print('==',sum1)
b=sum1
if (s==b):
	print("the number is smith numbers. ")
else:
	print("the number is not smith numbers. ")