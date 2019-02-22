import threading
import time
class myThread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
		print(threadID,name,counter)
	def run(self):
		print ("Starting " + self.name)
		print_time(self.name, self.counter, 5)
		print ("Exiting " + self.name)
def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime()))
      counter -= 1
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread3 = myThread(3, 'Thread-3', 3)
thread1.start()
thread2.start()
thread3.start()
