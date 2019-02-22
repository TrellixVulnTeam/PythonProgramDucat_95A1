# Genrator in the python code of the main function ...???

def my_gen():
	n=1
	print("This is the first page .")
	yield n
	n+=1
	print("This is the second page .")
	yield n
	n+=1
	print("This is the last page .")
	yield n
a = my_gen()
print(a)          # return class address of the generator file of the program of the python code.

# print(next(a))
# print(next(a))

for x in a:
	print(x)

	
'''
output ==

<generator object my_gen at 0x00D49FB0>

This is the first page .
1
This is the second page .
2
This is the last page .
3


'''