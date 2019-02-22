# thread  using in python code program ...??


import threading
import time 
def sample():
	for i in range(10):
		print(i,"hello world.",time.ctime())
		time.sleep(1)
		obj2 = threading.Thread(target = example)
		obj2.start()
def example():
	for j in range(10):
		print(j,"hello python code.",time.ctime())
		time.sleep(1)
		
obj1 = threading.Thread(target = sample)
obj1.start()
example()




'''
output ==

in the path of the main python code server path run in the current time with execute program  ...

0 hello world.
0 hello python code.
1 hello python code.
0 hello python code.
1 hello world.
1 hello python code.
2 hello python code.
0 hello python code.
2 hello world.
1 hello python code.
3 hello python code.
2 hello python code.
0 hello python code.
3 hello world.
1 hello python code.
3 hello python code.
4 hello python code.
2 hello python code.
0 hello python code.
4 hello world.
3 hello python code.
4 hello python code.
2 hello python code.
1 hello python code.
0 hello python code.
5 hello python code.
5 hello world.
1 hello python code.
3 hello python code.
4 hello python code.
2 hello python code.
6 hello python code.
6 hello world.
0 hello python code.
5 hello python code.
1 hello python code.
6 hello python code.
5 hello python code.
2 hello python code.
7 hello python code.
3 hello python code.
0 hello python code.
4 hello python code.
7 hello world.
1 hello python code.
4 hello python code.
8 hello python code.
6 hello python code.
7 hello python code.
3 hello python code.
0 hello python code.
5 hello python code.
8 hello world.
2 hello python code.
6 hello python code.
4 hello python code.
5 hello python code.
7 hello python code.
3 hello python code.
2 hello python code.
8 hello python code.
9 hello world.
9 hello python code.
0 hello python code.
1 hello python code.
1 hello python code.
8 hello python code.
9 hello python code.
3 hello python code.
6 hello python code.
7 hello python code.
2 hello python code.
0 hello python code.
4 hello python code.
5 hello python code.
6 hello python code.
9 hello python code.
3 hello python code.
8 hello python code.
7 hello python code.
2 hello python code.
5 hello python code.
4 hello python code.
1 hello python code.
2 hello python code.
9 hello python code.
3 hello python code.
6 hello python code.
7 hello python code.
8 hello python code.
5 hello python code.
4 hello python code.
5 hello python code.
3 hello python code.
7 hello python code.
4 hello python code.
8 hello python code.
9 hello python code.
6 hello python code.
7 hello python code.
8 hello python code.
6 hello python code.
5 hello python code.
9 hello python code.
4 hello python code.
6 hello python code.
9 hello python code.
7 hello python code.
8 hello python code.
5 hello python code.
6 hello python code.
9 hello python code.
8 hello python code.
7 hello python code.
8 hello python code.
7 hello python code.
9 hello python code.
8 hello python code.
9 hello python code.
9 hello python code.





%%%%%%%%%%%%%%%%%%%%%%%%%%%      NEXT OUTPUT   IN CURRENT TIME IN THE PROGRAM IN PATH OF CODE >>>


0 hello world. Wed Jan 16 23:11:13 2019
0 hello python code. Wed Jan 16 23:11:13 2019
1 hello python code. Wed Jan 16 23:11:14 2019
0 hello python code. Wed Jan 16 23:11:14 2019
1 hello world. Wed Jan 16 23:11:14 2019
1 hello python code. Wed Jan 16 23:11:15 2019
2 hello python code. Wed Jan 16 23:11:15 2019
0 hello python code. Wed Jan 16 23:11:15 2019
2 hello world. Wed Jan 16 23:11:15 2019
1 hello python code. Wed Jan 16 23:11:16 2019
2 hello python code. Wed Jan 16 23:11:16 2019
0 hello python code. Wed Jan 16 23:11:16 2019
3 hello world. Wed Jan 16 23:11:16 2019
3 hello python code. Wed Jan 16 23:11:16 2019
1 hello python code. Wed Jan 16 23:11:17 2019
3 hello python code. Wed Jan 16 23:11:17 2019
2 hello python code. Wed Jan 16 23:11:17 2019
4 hello python code. Wed Jan 16 23:11:17 2019
0 hello python code. Wed Jan 16 23:11:17 2019
4 hello world. Wed Jan 16 23:11:17 2019
1 hello python code. Wed Jan 16 23:11:18 2019
3 hello python code. Wed Jan 16 23:11:18 2019
5 hello python code. Wed Jan 16 23:11:18 2019
2 hello python code. Wed Jan 16 23:11:18 2019
5 hello world. Wed Jan 16 23:11:18 2019
0 hello python code. Wed Jan 16 23:11:18 2019
4 hello python code. Wed Jan 16 23:11:18 2019
5 hello python code. Wed Jan 16 23:11:19 2019
1 hello python code. Wed Jan 16 23:11:19 2019
4 hello python code. Wed Jan 16 23:11:19 2019
6 hello python code. Wed Jan 16 23:11:19 2019
3 hello python code. Wed Jan 16 23:11:19 2019
2 hello python code. Wed Jan 16 23:11:19 2019
6 hello world. Wed Jan 16 23:11:19 2019
0 hello python code. Wed Jan 16 23:11:19 2019
1 hello python code. Wed Jan 16 23:11:20 2019
4 hello python code. Wed Jan 16 23:11:20 2019
2 hello python code. Wed Jan 16 23:11:20 2019
7 hello python code. Wed Jan 16 23:11:20 2019
5 hello python code. Wed Jan 16 23:11:20 2019
0 hello python code. Wed Jan 16 23:11:20 2019
3 hello python code. Wed Jan 16 23:11:20 2019
7 hello world. Wed Jan 16 23:11:20 2019
6 hello python code. Wed Jan 16 23:11:20 2019
4 hello python code. Wed Jan 16 23:11:21 2019
7 hello python code. Wed Jan 16 23:11:21 2019
5 hello python code. Wed Jan 16 23:11:21 2019
2 hello python code. Wed Jan 16 23:11:21 2019
1 hello python code. Wed Jan 16 23:11:21 2019
6 hello python code. Wed Jan 16 23:11:21 2019
8 hello world. Wed Jan 16 23:11:21 2019
3 hello python code. Wed Jan 16 23:11:21 2019
8 hello python code. Wed Jan 16 23:11:21 2019
0 hello python code. Wed Jan 16 23:11:21 2019
1 hello python code. Wed Jan 16 23:11:22 2019
7 hello python code. Wed Jan 16 23:11:22 2019
6 hello python code. Wed Jan 16 23:11:22 2019
8 hello python code. Wed Jan 16 23:11:22 2019
9 hello python code. Wed Jan 16 23:11:22 2019
3 hello python code. Wed Jan 16 23:11:22 2019
0 hello python code. Wed Jan 16 23:11:22 2019
5 hello python code. Wed Jan 16 23:11:22 2019
2 hello python code. Wed Jan 16 23:11:22 2019
4 hello python code. Wed Jan 16 23:11:22 2019
9 hello world. Wed Jan 16 23:11:22 2019
5 hello python code. Wed Jan 16 23:11:23 2019
6 hello python code. Wed Jan 16 23:11:23 2019
4 hello python code. Wed Jan 16 23:11:23 2019
8 hello python code. Wed Jan 16 23:11:23 2019
2 hello python code. Wed Jan 16 23:11:23 2019
1 hello python code. Wed Jan 16 23:11:23 2019
9 hello python code. Wed Jan 16 23:11:23 2019
3 hello python code. Wed Jan 16 23:11:23 2019
7 hello python code. Wed Jan 16 23:11:23 2019
0 hello python code. Wed Jan 16 23:11:23 2019
4 hello python code. Wed Jan 16 23:11:24 2019
8 hello python code. Wed Jan 16 23:11:24 2019
9 hello python code. Wed Jan 16 23:11:24 2019
7 hello python code. Wed Jan 16 23:11:24 2019
3 hello python code. Wed Jan 16 23:11:24 2019
5 hello python code. Wed Jan 16 23:11:24 2019
2 hello python code. Wed Jan 16 23:11:24 2019
6 hello python code. Wed Jan 16 23:11:24 2019
1 hello python code. Wed Jan 16 23:11:24 2019
6 hello python code. Wed Jan 16 23:11:25 2019
7 hello python code. Wed Jan 16 23:11:25 2019
8 hello python code. Wed Jan 16 23:11:25 2019
3 hello python code. Wed Jan 16 23:11:25 2019
4 hello python code. Wed Jan 16 23:11:25 2019
5 hello python code. Wed Jan 16 23:11:25 2019
9 hello python code. Wed Jan 16 23:11:25 2019
2 hello python code. Wed Jan 16 23:11:25 2019
7 hello python code. Wed Jan 16 23:11:26 2019
6 hello python code. Wed Jan 16 23:11:26 2019
4 hello python code. Wed Jan 16 23:11:26 2019
5 hello python code. Wed Jan 16 23:11:26 2019
8 hello python code. Wed Jan 16 23:11:26 2019
9 hello python code. Wed Jan 16 23:11:26 2019
3 hello python code. Wed Jan 16 23:11:26 2019
6 hello python code. Wed Jan 16 23:11:27 2019
8 hello python code. Wed Jan 16 23:11:27 2019
9 hello python code. Wed Jan 16 23:11:27 2019
7 hello python code. Wed Jan 16 23:11:27 2019
5 hello python code. Wed Jan 16 23:11:27 2019
4 hello python code. Wed Jan 16 23:11:27 2019
6 hello python code. Wed Jan 16 23:11:28 2019
8 hello python code. Wed Jan 16 23:11:28 2019
9 hello python code. Wed Jan 16 23:11:28 2019
7 hello python code. Wed Jan 16 23:11:28 2019
5 hello python code. Wed Jan 16 23:11:28 2019
8 hello python code. Wed Jan 16 23:11:29 2019
9 hello python code. Wed Jan 16 23:11:29 2019
7 hello python code. Wed Jan 16 23:11:29 2019
6 hello python code. Wed Jan 16 23:11:29 2019
9 hello python code. Wed Jan 16 23:11:30 2019
8 hello python code. Wed Jan 16 23:11:30 2019
7 hello python code. Wed Jan 16 23:11:30 2019
9 hello python code. Wed Jan 16 23:11:31 2019
8 hello python code. Wed Jan 16 23:11:31 2019
9 hello python code. Wed Jan 16 23:11:32 2019


'''