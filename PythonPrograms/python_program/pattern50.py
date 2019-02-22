# print pattern on the digramm....???


a = 0
b = 1
arr = []
for i in range(4):
	c =  a + b
	a = b
	b = c
	arr.append(c)
#print(sum(arr))
sum1 = 0
sum2 = 0
for i in range(len(arr)-1,0,-1):
		sum1 += arr[i]
		print(' '*sum2+'*'*arr[i]+' '*((sum(arr)*2)-1-(sum1*2))+'*'*(arr[i]))
		sum2 = sum1
print(' '*sum2+'*'*arr[0])

'''
*****           *****
     ***     ***
	    ** **
		  *
'''
# when range change 4 to 5 ...???
'''
********                     ********
        *****           *****
             ***     ***
                ** **
                  *
'''