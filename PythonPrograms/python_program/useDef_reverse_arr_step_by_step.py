#140.  reverse array step.??

arr = [1,2,3,4,5,6]
# d= int(input('enter the no of reverse:'))
def reverse(arr,n):
    temp = arr[n]
    for i in range(n,0,-1):


        arr[i]=arr[i-1]
    arr[0]= temp
# for i in range(d):
reverse(arr,5)
print(arr)