# 1 **  date and time use by def ...???


import time

ticktock = time.time()

print("Number of ticks: ", ticktock)

'''
Output:
Number of ticks: 1465927104.951356
Number of ticks: 1545383805.541121

'''

# 2 **  Another program showing datetime module: 

from datetime import datetime

presentime = datetime.now()

print("NOW THE TIME IS:", presentime)
print("Todays Date is:", presentime.strftime('%Y-%m-%d') )
print("Year is:", presentime.year)
print("MOnth is:", presentime.month)
print("Day is:", presentime.day) 


'''
output ===

NOW THE TIME IS: 2018-12-21 14:46:45.631712
Todays Date is: 2018-12-21
Year is: 2018
MOnth is: 12
Day is: 21


'''




# 3 **  Python Program - Print Date and Time

import datetime
print("Want to print Today's Date and Time ? (y/n): ")
check = input();
if check == 'n':
    exit()
else:
    print("Today's date and time:")
    print(datetime.datetime.today())



'''
output ===


Want to print Today's Date and Time ? (y/n):
y

Today's date and time:
2018-12-21 14:47:00.340862
'''
