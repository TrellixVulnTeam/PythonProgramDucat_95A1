# Python Print Floyd Triangle    ????

# Python Program - Print Floyd Triangle

print("Enter 'x' for exit.")
ran = input("Upto how many line ? ")
if ran == 'x':
    exit();
else:
    rang = int(ran)
    k = 1
    for i in range(1, rang+1):
        for j in range(1, i+1):
            print(k, end=" ")
            k = k + 1
        print()
		
		
		
'''
output ===

Enter 'x' for exit.
Upto how many line ? 5
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

'''

