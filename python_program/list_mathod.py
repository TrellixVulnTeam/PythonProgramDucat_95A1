# list _ mathod using them test on the use in programming because run programming ....??

a=[1,2,3,4,5,6,7]
b=["ram","shyam","sita","gita","raju","sitaram","gajodher","ramji",185,789,546]
a.append(b)    #*1   # list a to all append list b in a then updated list a added all value in list a...
print(a)


a=[1,2,"ram","shyam"]
c=a.copy()      #*2
d=a.clear()     #*3
print(c)                # print a list to copy to all value in list print..  (sallow list to all values in list copy file.)
print(d)                # print o/t (none) ...     because the list has clear to full on the all values ..


a=["hello","ram",1,5,8,7896,45876,213654,45]
a.extend([2543])    #*4          (we cwn use this mathod to any list added in last so join always last index value (ex.  (-1)index always join the value))
print(a)

a.insert(1,389674589654587456)     #*5       (what value added in list which place we can used the insert mathod like that (ex..  1, added the 3 index of list they can used the mathod of index value..))
print(a)


a.index([5][0])    #*6             # index value ([5][3])     o/t == >>>   given 5th of third element in list value ..
print(a)
b=[12,354,4587,4569,789,65,65,65,78,65]
t=b.index(4587,0,3)       #*7      # we can create the value in list whose index value return in your o/t .  (ex=  4587   is list of 2nd index value.)
print(t)

l=a.count(65)       #*8    (count any value in list how many times so we can use the count value.)
print(l)

b=[12,354,4587,4569,789,65,65,65,78,65]
a=b.pop()           #*9    (using like a recycle bin work remove the list varriable in last index value and the used the stored deleted value we can used deleted value then u can use the pop mathod )
print(a)

b=[12,354,4587,4569,789,65,65,65,78,65]
print(b.pop(4))    #*10     (we can show the pop index they are delete the index value and so also the index value they are remove in list u can also restore the value again using the index value .)

b=[12,354,4587,4569,789,65,65,65,78,65]
b.remove(4587)      #*11   (we can used by this mathod the value can remove from user input list the used mathod also.)
print(b)

b=[12,354,4587,4569,789,65,65,65,78,65]
b.reverse()         #*12  (we can used the mathod so list has reverse but not sort also)   ==== as like reverse user input list so as it is reverse in that form.
print(b)

b=[12,354,4587,4569,789,65,65,65,78,65]
b.sort()          #*13    (we can use the mathod list sort in asending to descending order always..)
print(b)

b=[12,354,4587,4569,789,65,65,65,78,65]
b.sort(reverse=True)      #*14     (we can use the mathod in descending to asending order always we can write the mathod always.)
print(b)

b=[12,354,4587,4569,789,65,65,65,78,65]
del b[2]            #*15     (we can use the mathod of the value of index they are deleted this value.)
print(b)

b=[12,354,4587,4569,789,65,65,65,78,65]
del b[1:4];del b[1:9:5]      #*16  (we can use the mathod of the value of index they are deleted 0 to all value   or slice operter we can use the step by step value we can used always.)
print(b)

a=[1,2,3,4,5,6]
del b[:1]                  #*17   (we can used the mathod slice should be values before 1th index value del form list value)
print(a)

a=[1,2,3,4,5,6]
a.clear()
print(a)              #*18  (clear the list of all values .)


e="3.1458796"
print(e.isdecimal())                # o/t ===  false


f=3
print(f.isdecimal())

a="hello \t world"
print(a.isspace())                 # what input from user got true result.

a=" "    #   a='/t'
print(a.isspace())                 # what input from user got true result.


b="hello world "
print(b.istitle())                   # what input from user got true result.

d=",".join(["b","cv","got"])
print(d)