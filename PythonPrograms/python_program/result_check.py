a= int(input("enter the first subject mark:"))
b= int(input("enter the first subject mark:"))
c= int(input("enter the first subject mark:"))
d= int(input("enter the first subject mark:"))
e= int(input("enter the first subject mark:"))
f= int(input("enter the first subject mark:"))
result= (a+b+c+d+e+f)/6
print(result)
if result<33:
	print("candidate faild & grade 'f'")
elif result>=33 and result<45:
	print("candidate passesd & grade 'e'")
elif result>=45 and result<60:
	print("candidate passesd & grade 'd'")
elif result>=60 and result<70:
	print("candidate passesd & grade 'c'")
elif result>=70 and result<80:
	print("candidate passesd & grade 'b'")
elif result>=80 and result<90:
	print("candidate passesd & grade 'a'")
elif result<=100:
	print("candidate passesd & grade 's'")
else:
	print("invalid result & not candidate exam ")
