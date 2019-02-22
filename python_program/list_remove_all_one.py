l=[1,2,1,2,1,3,4,5,1,1,1,1]
k = l.count(1)
n = len(l) - 1
for i in range(n):
	if l[i] == 1:
		for j in range(i,n):
			l[j] = l[j+1]
		l[n-1] = l[i]
		n = n -i 
for i in range(k):
	l.pop()
print(l)
		
		
		
'''
l=[1,2,1,2,1,3,4,5,1,1,1,1]
list in all 1 deleted in list....
remove all 1.
'''


# python list remove 1 ...??


l=[1,2,2,2,1,1,1,4,5,6,1,1,1]
while(1 in l ):
	l.remove(1)
print(l)