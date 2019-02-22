class Car:
    def drive(self):
        print ('driving. maxspeed ')
class abc(Car):
	def drive(self):
		print("in abc")
a=abc(),Car()
a[1].drive()
a[0].drive()