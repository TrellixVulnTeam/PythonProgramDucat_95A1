# one dimention array ...???
# Python Program - One Dimensional Array



#print("Enter 'x' for exit.")
n = int(input("How many element you want to store in the array ? "))
if n != 'x':   
    arr = []
    for i in range(1, n+1):
        arr.append(i);
    print("\nElements in Array are:")
    for i in range(0, n):
        print(arr[i], end=" ")
		
		
		
'''
output ==

Enter 'x' for exit.
How many element you want to store in the array ? 9

Elements in Array are:
1 2 3 4 5 6 7 8 9


How many element you want to store in the array ? 15

Elements in Array are:
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

'''