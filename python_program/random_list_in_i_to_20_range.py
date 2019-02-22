#128.  Generate Random Numbers from 1 to 20 and Append Them to the List:   ...>>
        # random value -- the value of no is surpised to you for any value and print them any num...??
import random
list=[]
n=int(input("enter the no:"))
for i in range(n):
    list.append(random.randint(1,20))        # it is formula used in the range of any int numbers...??
    # any int num print the random of any integer no.
print(" random number in list: ",list)