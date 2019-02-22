#144. using the sort list according to second sublist mathod.  >>

a=[['a',34],['b',21],['c',64]]            # print list in sublist from.
for i in range(1,len(a)):                # range of list a  in length .
    for j in range(0,(len(a)-i-1)):          # range of j is from len(a)-i-1 .
        if a[j][1]> a[j+1][1]:           # condition of the list value according to the sublist value .
            temp = a[j]                  # store the value in temp = value a[j]
            a[j]=a[j+1]                  # a[j] has incresed value in list.
            a[j+1]=temp                  # a[j+1] in store are equal to temp again.
print(a)
