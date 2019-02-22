import threading
class Call(threading.Thread):
	def run(self):
		for a in range(10):
			print(a,threading.currentThread().name)
o=Call(name="A")
ob=Call(name="B")
obj=Call(name="C")
o.start()
ob.start()
obj.start()