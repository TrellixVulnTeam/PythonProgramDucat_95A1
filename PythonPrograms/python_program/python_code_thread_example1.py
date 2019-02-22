# thread  using in python code using in the time in current time show in the path runserver in cmd show time program ...??


import threading
import time 
def sample():
	for i in range(10):
		print(i,"hello world.",time.ctime())
		time.sleep(1)
		
def example():
	for j in range(10):
		print(j,"hello python code.",time.ctime())
		time.sleep(1)
		
obj1 = threading.Thread(target = sample)
obj2 = threading.Thread(target = example)

obj1.start()
obj2.start()


'''
output ==
# using in time interval 1 sec set in the progarm code work the giving time interval ..  with show in cmd prompt the current time run in path.


0 hello world. Wed Jan 16 23:05:09 2019
0 hello python code. Wed Jan 16 23:05:09 2019
1 hello python code. Wed Jan 16 23:05:10 2019
1 hello world. Wed Jan 16 23:05:10 2019
2 hello world. Wed Jan 16 23:05:11 2019
2 hello python code. Wed Jan 16 23:05:11 2019
3 hello world. Wed Jan 16 23:05:12 2019
3 hello python code. Wed Jan 16 23:05:12 2019
4 hello python code. Wed Jan 16 23:05:13 2019
4 hello world. Wed Jan 16 23:05:13 2019
5 hello world. Wed Jan 16 23:05:14 2019
5 hello python code. Wed Jan 16 23:05:14 2019
6 hello python code. Wed Jan 16 23:05:15 2019
6 hello world. Wed Jan 16 23:05:15 2019
7 hello world. Wed Jan 16 23:05:16 2019
7 hello python code. Wed Jan 16 23:05:16 2019
8 hello python code. Wed Jan 16 23:05:17 2019
8 hello world. Wed Jan 16 23:05:17 2019
9 hello world. Wed Jan 16 23:05:18 2019
9 hello python code. Wed Jan 16 23:05:18 2019

'''