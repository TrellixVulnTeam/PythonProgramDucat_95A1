# Python Program to Generate a Random Number ??

import random
a=int(input("enter the first number == "))
b=int(input("enter the second number == "))
c=random.randint(a,b)
print("random number in range a to b ",c)

'''
a=45
b=96
output == 66
# next run again ==>>
a=45
b=96
output == 76
'''

# Python Program to Generate a Random Number ??   (another mathod random value in range ...??)

import random 
n=int(input("enter the range "))
print("random number in range == ",random.randrange(1,n+1))

'''
enter the range = 60
output == 13
'''

# Python Program to Generate a Random Number ??   (another mathod random value in range ...??)

import random 
n=int(input("enter the range "))
c=random.randrange(1,n+1,2)
print("even random number in range == ",c)


'''
enter the range = 60
output == 44  (even random number)
'''


# Python Program to Generate a Random Number ??   (another mathod random value in range ...??)


x=float(input("enter the number "))
random.random()        # Random float x, 0.0 <= x < 1.0

'''
output == 0.37444887175646646
'''


x=float(input("enter the number "))
c=random.uniform(1, 10)  # Random float x, 1.0 <= x < 10.0
print("random number in any uniform value ",c)

'''
1.1800146073117523
'''

d=random.randint(1, 10)  # Integer from 1 to 10, endpoints included
print("randomly print the any int number in given range",d)

'''  output ===
7
'''

d=random.randrange(0, 101, 2)  # Even integer from 0 to 100
print("any even number randomly in given range : ",d)

'''  output == 
26
'''


c=random.choice('abcdefghij')  # Choose a random element
print("any type of randomly choice the given element : ",c)
''' output == 
'c'
'''


items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items)
print("any type of squence form == ",items)

'''   output ==== 
[7, 3, 2, 5, 6, 4, 1]
'''


a=[1, 2, 3, 4, 5,45,78,89,658,79]
c=random.sample(a,  5)  # Choose 5 elements
print("any element randomly got ",c)

'''   output ====
[4, 1, 5,89,45]
'''


