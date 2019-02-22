#84.     Displays which Letters are in the Two Strings but not in Both ..??


str1= input('enter the string:')
str2= input('enter the string:')
a= set(str1)         # a in set form of string value.
b= set(str2)         # b in set form of string value.
  # e = a^b     (a to bitwise b = a union b - a intersection b)
c= a.union(b)        # a and b string charter to both combined but not repeat write once.
d= a.intersection(b)     # a and b commom charter print.
e=c-d       # charter are two string but not in both = union of a and b - intersection of a and b.
             # ( a ^ b = a U b - a intersetion b )
for x in e:
    print(x)