'''
Variable Scope:-
	Local with in function
	Global entire application

a=5#global
def sample():
	a=25#local
	print('in sample',a)
sample()	
print('in main',a)
'''
'''
a=5#global
def sample():
	global a
	a=25#global
	print('in sample',a)
sample()	
print('in main',a)
'''
'''
a=5#global
def sample():
	print('in sample',a)
sample()	
print('in main',a)
'''
###Function With Arguments.
'''
def sample(a,b):
	print(a,'+',b,'=',a+b)
sample(5, 4)	
'''
##Default Arguments
'''
def sample(a=0,b=0):
	print(a,'+',b,'=',a+b)
	
sample(4)
'''
##args(Arguments)
'''
def add(*args):
	sum=0
	for x in args:
		sum+=x
	print("Total : ",sum)
add(54,4,4,43,5,4,6,54,6,5,34,3,4,3,5)	

def greet(*names):
	for name in names:
		print("Hello",name)
greet("Ram","Alex","Google","Jarvis")
'''

##kwargs (KeyWord Agguments)
'''
def sample(**kwargs):
	print(kwargs)
sample(name="Ram",Class=7,age=14)	
'''

###Function With Return Type:-

#def sample():
#	a=int(input("Enter First Number: "))
#	b=int(input("Enter Second Number : "))
#	c=a+b
#	return c, a, b
#
#x,y,z=sample()
#print(x)
#print(y)
#print(z)
'''
import time
import calendar
#print(dir(calendar))
#print(help(calendar))
print(calendar.month(2019,1))
#print(time.ctime())
print(calendar.calendar(2019))
'''
'''
import calendar as c
print(c.month(2019,1))
'''
'''
from calendar import month
print(month(1700,2))
'''
'''
import utility as u
u.add(8,7,4,51)
'''
import utility as u
x=u.add(46,34,7,4,68)
print(x)

#pip install module_name
#pip uninstall module_name
'''
lambda

lambda operator or lambda function is used for creating 
small, one-time and anonymous function objects in Python.
Syntax:-
	lambda arguments : expression

add = lambda x,y : x + y 
b=add(5,4)
print(b)


filter(function_object, iterable_object) 




a = [1, 5, 4, 6, 8, 11, 3, 12]
add = lambda x : x % 2 == 0 
b = filter(add, a)
print(list(b))

a= [1, 5, 4, 6, 8, 11, 3, 12]
b = tuple(map(lambda x: x * 2 , a))
print(b)
'''
a = [{'name': 'java', 'points': 8}, 
		{'name': 'python', 'points': 10},
		{'name': 'php', 'points': 7},
		{'name': 'Ruby', 'points': 8},
		{'name': 'React-native', 'points': 9},
		{'name': 'React-JS', 'points': 6},
		{'name': 'Angular', 'points': 5},
		]
print(list(filter(lambda x : x['points'] == 8, a)))

new_list = [expression(i) for i in iterable_object if expression]


a=[i for i in range(1,100,2)]
print(a)

a=[i * i for i in range(5) if i % 2 == 0]
print(a)


list1 = [3,4,5]
multiplied = [item*3 for item in list1] 
print(multiplied)


listOfWords = ["this","is","a","list","of","words"]
items = [word[0] for word in listOfWords]
print(items)

a= [x+y for x in [10,30,50] for y in [20,40,60]]
print(a)

values = [1,2,3,4,5]     
myDict = {i:i*i for i in values}   
print(myDict)  

sDict = {x.upper(): x*3 for x in 'coding'} 
print (sDict) 


newdict = {x: x**3 for x in range(10) if x % 2 == 0} 
print(newdict)

with open('sample.txt','w') as f:
	f.write("Hello Python")
	print(f.closed)
print(f.closed)

class Error(Exception):
   """Base class for other exceptions"""
   pass

class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass

class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass

number = 10

while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
       print()
   except ValueTooLargeError:
       print("This value is too large, try again!")
       print()

print("Congratulations! You guessed it correctly.")