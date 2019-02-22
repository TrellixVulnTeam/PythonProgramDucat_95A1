# break , continue , pass statement :
# pass statement  =====  pass the loop value to next loop or value donot distube any one loop/value ...
# continue statement ==== continue check condition and skip that value in condition and continue all value/loop print all value but not print for condition skip value for condition ....
# break statement ==== braek use the value and loop outside any value ....


for x in range(5):
	if x==2:
		pass
	print(x,"hello world python")
	
'''
o/t ====                # all value print.
0 hello world python
1 hello world python
2 hello world python
3 hello world python
4 hello world python
'''

for x in range(5):
	if x==2:
		continue
	print(x,"hello sir")
	
'''
o/t ====                  # skip for x==2 value and all value print ..
0 hello sir
1 hello sir
3 hello sir
4 hello sir

'''


for x in range(5):
	if x==2:
		break
	print(x,"thank you")
	
'''                       # break loop for x==2 condition in before each value print but not equal and after not print any value for that ...
o/t ====
0 thank you
1 thank you

'''