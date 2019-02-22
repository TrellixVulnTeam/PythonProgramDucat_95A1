#109.  Flatten a List without using Recursion .??

a=[[1,[[2]],[[[3]]]],[[4],5]]
flat =lambda l: sum(map(flat,l),[]) if isinstance(l,list) else [l]
print(flat(a))
