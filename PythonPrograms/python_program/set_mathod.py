# set mathod implimented to any program ...??

# set can not used the index mathod because i am not understood the value what is index value then not used the index mathod....


a={1,2,3,4,8,(78,98,45,126),"hello","world","don",11.2,5.6,8j}
print(a,type(a))        # create a set but not in order of index so value all index where are upcoming so we ingore the index value in set ...


a.add(5)
print(a)                 # set any one value add so use the this mathod ..


a.update({105,789,"lalu"},[120,1000,78.36598])                             # set any multiple  value add so use the update  mathod ..
print(a)                                      # set used update mathod so tuple,list,set implemented but not used the any breakect update the only values .


a={1,2,5,2,3,4,5,8,7,9,65,"hello","hello","set"}
print(a)                         # set not contained the duplicated value .


a.discard(5)           # discard any value of set is delete value from user key value ...(but any value of key user input but not the set value so ignore this value any program run to next part ...)
print(a)


a.remove(9)                # remove any value of set value input in remove key .. (but any value of the key value is not in set so error find   find key error..)
print(a)


# diff b/w discard and remove ===>>>   discard the any value set value are not but pass the program in next line but remove given key error ...

a=set("hello458796485963")                # any string value seperated by set mathod not int type...("hello"== {h,e,l,o})  and int not iterate value so not perform the set value..
print(a)


a.pop()           # pop mathod remove always 1st index of updated set but we can not seen what is the element remove in set b/c update set i can no what is the index of first so i can not understood..
print(a)


a.clear()             # all set value clear so no element of the set . (o/t ===   set())
print(a)



              # python set operation we can use in the program value of .....
			  
a={2,5,4,7,8,9,10,"hello","low"}
b={5,78,12,4,9,45,"python","shree","raj","low"}
print(a-b)                         # a and b difference of set value ..
print(a.difference(b))
print(b-a)
print(b.difference(a))


print(a|b)                         # a and b two set both are union ..
print(a.union(b))
print(b|a)
print(b.union(a))


print(a&b)                          # a and b two set both are intersection ..
print(a.intersection(b))
print(b&a)
print(b.intersection(a))


a={2,5,4,7,8,9,10,"hello","low"}
b={5,78,12,4,9,45,"python","shree","raj","low"}
print(a^b)                          # and b two set both union and intersection difference of that value that is ...
print(a.symmetric_difference(b))           #  ex..(a^b = a|b  -  a&b)
print(b^a)                                 # means ===  (a.symmetric_difference(b)  ===  a.union(b)  -  a.intersection(b))
print(b.symmetric_difference(a))           # o/t ==   {2, 'shree', 'raj', 7, 8, 10, 12, 45, 78, 'hello', 'python'}


print(a.difference_update(b))        # a in difference_update value so print(a)      otherwise given o/t == none
print(a)                              # o/t === {2, 7, 8, 10, 'hello'}       # a ki all lefted value print in update of a value..(both same value remove that set)
print(b.difference_update(a)) 
print(b)


a={2,5,4,7,8,9,10,"hello","low"}
b={5,78,12,4,9,45,"python","shree","raj","low"}
print(a.intersection_update(b))        # Update the set with the intersection of itself and another   
print(a)                                # o/t ===  {9, 4, 5, 'low'}         # print only common value of both sets ...
print(b.intersection_update(a))
print(b)


a={1,2,7,8}                                   #  Return True if two sets have a null intersection .... otherwise given o/t is false.
b={4,5,9}
print(a.isdisjoint(b))
a={4,5,6}                                     # any value in common of both set so return the false output...
b={4,8,9}
print(a.isdisjoint(b))


a= {1,2,3,4,5,6,7}
b={1,2,3}
print(a.issubset(b))    #o/t== (False)  # b is not subset of a..           (subset means ===>>>    compare set in present in given set (com set is present in the given set))
print(a.issuperset(b))  #o/t== (True)   # a is superset of b.               (superset means the set greater to compare set ((com set < given set))))
print(b.issubset(a))    #o/t== (True)   # b is subset of a.
print(b.issuperset(a))	#o/t== (False)  # b is not superset of a.


# membership operation  check True or False ....

a=set("apple")
print(a)
for a in a:
	print('a' in a)
	print('l' not in a)          # given output false b/c outside the loop print value to check condition is false..  (otherwise given True ..)


a=set("4587965874962329321324821321564321321562132456")
print(a)         # given o/t ===  {'2', '7', '3', '4', '5', '9', '6', '8', '1'}

print(all in a)         # all in a (o/t ===    False)
print(any in a)         # any in a (o/t ===    True)


list=[]
for i in set("power point excel "):
	print(i)                            # every value of set in i .
	list.append(i)
print(list)          # collect all set value in the list storage .. 



a=set("4587965874962329321324821321564321321562132456")
print(len(a))
#   print(sum(a))          # not work b/c the value of str to not sum to str so given problem
#   print(a.sorted())      # can not used in the mathod b/c set convert list after sort one and after convert again set form ....
print(min(a))              # min number of set , max number of set ...
print(max(a))
print(enumerate(a))         # o/t given (<enumerate object at 0x03222580>)     b/c the mathod not used in the index value os any set so result give that is...

''' 
                                    ############      frozenset  of sets .....    #################
									
#  diff of the frozenset and set ====>>>  only one frozenset contained all value and it is immutable lenght of set but set is oposite only mutable value..
 frozenset cannot applied add,update ,del,discard,remove ....  and use for fix value not change,:::::     but set can implimented all programs so can change for length value..  
but frozenset cannot change of length because not implemented the another add type, update type no used it ... 
 '''
 
#   how to create the frozenset  ....??
 
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
print(A)
print(B)
'''
output === 
frozenset({1, 2, 3, 4})
frozenset({3, 4, 5, 6})
'''
print(A.isdisjoint(B))
# o/t == False
print(A.difference(B))
#  output === frozenset({1, 2})
print(A | B)
# output === frozenset({1, 2, 3, 4, 5, 6})
'''
print(A.add(9))
# cannot used the mathod in frozenset because given error...
# o/t ====   AttributeError: 'frozenset' object has no attribute 'add'
'''