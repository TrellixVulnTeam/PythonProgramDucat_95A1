# Python Program - Print Date and Time

import datetime
print("Want to print Today's Date and Time ? (y/n): ")
check = input("date and time: ")
if check == 'n':
    exit()
else:
    print("\nToday's date and time:")
    print(datetime.datetime.today())
	
	
	
'''
output ==

Want to print Today's Date and Time ? (y/n):
date and time: y

Today's date and time:
2018-12-16 23:03:36.145457
'''