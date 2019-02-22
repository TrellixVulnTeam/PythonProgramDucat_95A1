#146.   any sort  value in tuple is increased in list form and sort them value in tuple values :..>>

def last(n):          # define the key function...>>
    return n[-1]

def sort(tuples):                              # sort the tuple at the last key mathod.
    return sorted(tuples, key=last)

list = [(2,2),(1,4),(1,3)]       # print list in tuple.
l = sort(list)        # sort list increased in tuple form. >>
print(l)