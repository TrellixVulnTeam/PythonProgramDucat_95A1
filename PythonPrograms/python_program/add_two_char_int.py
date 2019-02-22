#  Python Add Two Numbers  ????

a= input("enter the user input : ")
b= input("enter the user input : ")
c= a+b
print("add_string : ",c)
d= int(a) + int(b)
print("add value : ",d)


'''
output  1  ======
enter the user input : ram
enter the user input : raja
add_string :  ramraja
Traceback (most recent call last):
  File "add_two_char_int.py", line 7, in <module>
    d= int(a) + int(b)
ValueError: invalid literal for int() with base 10: 'ram'

'''

'''
output  2  =======
enter the user input : 789
enter the user input : 546
add_string :  789546
add value :  1335
'''