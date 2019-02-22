# Python Display Calendar  ???

# Python program to display calendar of given month of the year

# import module
import calendar

# yy = 2014
# mm = 11
# To ask month and year from the user
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))

'''
output ====
Enter year: 2018
Enter month: 12
   December 2018
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31

'''

'''
output ===
Enter year: 2019
Enter month: 01
    January 2019
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31


'''