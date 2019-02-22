import threading
import time
a=int(input("Enter Range : "))		
class MyThread(threading.Thread):
	def run(self):
		for x in range(a):
			print(x,threading.currentThread().name)
			time.sleep(1)
m=MyThread(name="A")
m.start()