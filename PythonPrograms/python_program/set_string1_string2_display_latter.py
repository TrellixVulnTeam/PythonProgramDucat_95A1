#83.    Displays which Letters are in the First String but not in the Second .??

str1= input('enter the string:')
str2= input('enter the string:')
a= set(str1)        # str1 in set form spertly all variable.
b= set(str2)         # str1 in set form spertly all variable.
c= a-b               # variable of the a is not to be b .
 # print(c)        # print set form.
for x in c:
    print(x)          # all set value loop from .