# dictionary mathod ===>>>???

# 1 ***     key are unique .
# 2 ***     imutable ==>>>    tuple ,int ,str, frozenset ....


a= {1:"hello",2:"world",3:"python",1:"value"}        # create dictionary any key and value add to dictionary value
print(a,type(a))     
# note --->>>  key has unique but value has comes on the last key value update the key of value print in dict.
# output ===  {1:"value",2:"world",3:"python"}


a= {frozenset({1,2,3}):"hello",2:"world",3:"python"}        # create dictionary any key and value add to dictionary value
print(a,type(a))


a [2]="sita"
print(a)
 
a ["name"]=45896
print(a)


b={}                                       # empty dictionary ..  
print(b,type(b))

c={'name':"Ram","value":[1,78,98,65,123]}     # in {key:value}   convert dict form ..
print(c,type(c))

d=dict({1:"ram",2:"shyam",4:"sita",5:"ray"})    # in list value in given tuple form is key and values has given the form of line ..
print(d)

e=dict([(2,78),(4,178),(6,278),(8,378),(10,478),(12,578)])
print(e)

print(e[2],e[4])    # print(any key value of dict use the dict[key=4])      #  o/t == 78   178

print(e.get(8))          # dict.get using the address of key find the value of given key ...         #  o/t == 378

a={2:"name",4:"class",6:"school"}      # in dict key value is update the next key value is replace any value to change value ..
a[6]="collage"
print(a)

a[8]="father name"                    # in dict key value next add in dict ..   (only one value update ..)
print(a)


squares = {1:1, 2:4, 3:9, 4:16, 5:25, 6:36}  
# remove a particular item
# Output: 16                               # pop remove the key value 4th   but given output this key of value ===  16


print(squares.pop(4))  
# Output: {1: 1, 2: 4, 3: 9, 5: 25, 6:36}


print(squares)
# remove an arbitrary item
# Output: (6:36)


print(squares.popitem())                   # remove the popitem so remove last key delete in dict..
# Output: {1:1, 2: 4, 3: 9, 5: 25}

print(squares)
# delete a particular item                 # any key value delete in dict so del dict[key=value]

del squares[5]  
# Output: {1:1, 2: 4, 3: 9}

print(squares)
# remove all items
squares.clear()
# output:                                  # full clear dict all value ...   empty no value and key   so output comes       sapce..

 
 
print({}.fromkeys(["apple","mango","banana"],4))       #    like that  ====   dict.fromkeys(["examples:::"],key value all value in same ..)
# output ===   {'apple': 4, 'mango': 4, 'banana': 4}


marks = {}.fromkeys(['Math','English','Science'], 0)                  # dict.fromkeys([list item],,value of keys..)
# Output: {'English': 0, 'Math': 0, 'Science': 0}
print(marks)


for item in marks.items():
    print(item)
# Output: ['English', 'Math', 'Science']
list(sorted(marks.keys()))


squares = {x: x*x for x in range(6)}                               # in range value of the given key in use the key value in value after add the key all value in dict ..
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)

cubes = {x: x**3 for x in range(6)}                               # dict same from the keys value in the format of cubes of keys..
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(cubes)

dict={}                                                           # dict={} and in range value of key values multi,pow same the all value format is added the same value format after add one by one process...
for x in range(10):
	dict[x] = x**4
print(dict)



squares = {}                                               # dict value update automatically condition given only even value of square print in dict form..
for x in range(100):
	if x%2==0:
		squares[x] = x*x
print(squares)

   
odd_squares = {x: x*x for x in range(100) if x%2 == 1}
# Output: {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(odd_squares)                           # dict value update automatically condition given only odd value of square print in dict form.



squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
                                     # check key vlaue in dict from present key in dict then given the output is True..  otherwise  False..
print(1 in squares)
# Output: True  

print(2 not in squares)
# Output: True
# membership tests for key only not value

print(49 in squares)
# Output: False
# membership tests for key only not value....     (b/c  value 49 in present but output given the False..)


squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])

'''       #  print key values of dict form ...   all value print in the i is key so presented the all values in dict...??
output ====
1
9
25
49
81
'''


squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}         #  len find the what is keys there in dict  present in len of dict ===   no of keys..
# Output: 5

print(len(squares))
# Output: [1, 3, 5, 7, 9]                                   #  sorted(dict) ==   in use  dict the keys of all values in sort of key value assending to discending order ....
print(sorted(squares))


a={1: 1, 3: 9, 5: 25, 7: 49, 9: 81, 10:1250}        # given empty dict when given output is same..
print(any in a)                             # any one in a get true ...(like that 1,3,5,9,10 ...  etc..)     output === False
print(1 in a)  								# any one key is 1 present in dict then given output ===  True ..
print(11 in a)                              # any value of key no is not present then given False .
print(all in a)                             # all value in present in dict given output == False .



'''
dict  can not used the cmp mathod .
'''

a={"name":"saurabh", "class":"pG", "job":"kanpur" , "post":"Smt(senior manager of it devloper)" , "salary":"1.25 lakh"}
print(a.keys())
print(a.values())


# nested dictionary   *******

s = {'name': {'first':'will','last':'smith'}, 'age':17 , 'occup':['teaching ','superviser','manager']}
print(s['name']['first'])
s['name']['middle'] = 'coras'
s['occup'].append('HR')
print(s)

'''
output ==

will
{'name': {'first': 'will', 'last': 'smith', 'middle': 'coras'}, 'age': 17, 'occup': ['teaching ', 'superviser', 'manager', 'HR']}

'''

a = {1:"ram"}
b = {2: "shyam"}
a.update(b)
print(a)
print(1 in a)
for x in a:
	print(x)     # x store all key value not value.
	print(x,a[x])    # a[x]  == value print .
	
'''
output ==
output ==
{1:"ram",2:"shyam"}

true

1
2

1 ram
2 shyam
'''
	
