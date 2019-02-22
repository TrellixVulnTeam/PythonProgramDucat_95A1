#2. average of given list ..??


list = []
n= int(input("enter the no of terms:"))
for i in range(1,n+1):
    m = int(input("enter the no:"))
    list.append(m)
# print(list)
sum=0
for j in list:
     # print(j)
    sum=sum+j
# print(sum)
avg = (sum)/n
print("average of list =",avg)