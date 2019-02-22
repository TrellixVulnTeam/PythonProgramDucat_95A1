# Itration mathod of python code in example value ==>>>


a = [1,2,3,4,5,6,7,8,9,10]
b = a.__iter__()
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())



'''
output ==
1
2
3
4
5
6
7
8
9
10


'''

a = "hello"
b = iter(a)
print(next(b))                   ##### h print one times call then print1 times h.#####
for x in a:
	print(x)



'''
output==
one time call then print only one world but print in the for loop then ###  stop itration value error show  ###
h
h
e
l
l
o

'''


