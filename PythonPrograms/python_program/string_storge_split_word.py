# string stroge any word with given the index value print them out of the range value so print the value of this word uses on the index value ...????
# count the char of index value also in string ..??
# condition also check in any string char ..??

a=" They are bunch of characters . In other words they are identified as contiguous ( IN SEQUENCE ) set of characters . Subset of strings can be taken using slice operator "
b=a.split()
'''print(b)       
' not used count ' then print the total word in string one by one print that ...??
'''
c=0
for x in b:
	if (x=="are"):         
'''
condition can not use in the string program so not print the only condition value and index , both the print count and word
'''
		print(x)
		c=c+1
print("count of word in given string :  == ",c)
