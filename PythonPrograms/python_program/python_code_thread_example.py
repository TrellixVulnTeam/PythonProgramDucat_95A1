# thread  using in python code program ...??

import threading
import time 
def sample():
	for i in range(10):
		print(i,"hello world.")
		time.sleep(1)
		
def example():
	for j in range(10):
		print(j,"hello python code.")
		time.sleep(1)
		
obj1 = threading.Thread(target = sample)
obj2 = threading.Thread(target = example)

obj1.start()
obj2.start()


'''
output === 
# using in time interval 1 sec set in the progarm code work the giving time interval ..

0 hello world.
0 hello python code.
1 hello world.
1 hello python code.
2 hello world.
2 hello python code.
3 hello world.
3 hello python code.
4 hello world.
4 hello python code.
5 hello world.
5 hello python code.
6 hello world.
6 hello python code.
7 hello world.
7 hello python code.
8 hello world.
8 hello python code.
9 hello world.
9 hello python code.


'''