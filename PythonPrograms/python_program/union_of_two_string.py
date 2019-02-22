#85.   Displays which Letters are Present in Both the Strings . ??
                                    # union of two string value :
str1= input('enter the string:')
str2= input('enter the string:')
a= set(str1)        # str1 in set form spertly all variable.
b= set(str2)         # str1 in set form spertly all variable.
c= a.union(b)         # c= a|b   ( '|'  - union symbol )
             # variable of the a is not to be b .
 # print(c)
                       #  print set form.
for x in c:
    print(x)
                                    # Intersection of two string value :

str1= input('enter the string:')
str2= input('enter the string:')
a= set(str1)        # str1 in set form spertly all variable.
b= set(str2)         # str1 in set form spertly all variable.
c= a.intersection(b)
             # variable of the a and b all str in commom charter print .
 # print(c)
                       #  print set form.
for x in c:
    print(x)
