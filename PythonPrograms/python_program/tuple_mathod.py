#  tuple mathods all print function ...??
# tuple is iterate object(can notbe change) and list are irterate object(can be change).
# tuple can be sort mamory and sort getsize and list lagerst mamory and getsize is high .
# tuple contains any value and any class store present (),and list same process but contains any value [].

a=(1,2,5,4,6,9,8,7,6,3,2,5,1,4,"hello","world",3.1254,2.52)      # tuple is itreable object (it is can not change)
print(a,type(a))


a=(1,2,5,4,6,9,8,7,6,3,2,5,1,4,"hello","world",3.1254,2.52)       # tuple can be change any process then we can convert the tuple to list any process u can do and change again in tuple .
b=list(a)
b.append("ducat")        # in tuple change in list and append any value of list after convert in tuple.
print(b)
del b[2]           # del in tuple use only can do this mathod but u can change in tuple to list 
b.remove(7)        # we can use this mathod any element in the tuple to convert on list so list can remove this value and u can use the function change in tuple to list.
a=tuple(b)
print(a)

a=(1,2,5,4,6,9,8,7,6,3,2,5,1,1,[4,"hello","world"],3.1254,2.52)     # tuple inner the list so append any value in list index so given o/t.
a[14].append("python")                              # in tuple list add any value in list index.
print(a)

print(a.count(1))          # using counter in any value in tuple .

print(a.index(5,1,8))       # print this value of index in any tuple or list both same use in tuple/list,(value,start,stop).



#   can not change any value in tuple a,b ...??
# all mathod given output not given error because the tuple value can not change in a to b . so all result given---.
a=("ram","shyam","sita",5,45,78,98,65,1.12,3.45)
b=("ram","shyam","sita",5,45,78,98,65,1.12,3.45)
print(a+b)           # operation mathod.
print(a*3)           # repliction (product mathod )
print(5 in a)        # membership relation mathod.
print(5 not in b)
print(len(a))         # length mathod.
for x in a:           # iteration mathod   (saprate mathod ..)
	print(x)
	
	
