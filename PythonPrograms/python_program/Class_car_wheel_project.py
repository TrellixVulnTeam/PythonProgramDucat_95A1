# 1. Class use car fuction called ..???


class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

mustang = Car('Ford', 'Mustang')
print(mustang.wheels)
print(Car.wheels)



# output == 4
# output == 4


# 2. Class use car fuction called ..???

class Car():
    ...
    def make_car_sound(self):
        print('VRooooommmm!')
		
a = Car()
a.make_car_sound()


# output ==     VRooooommmm!


# 3. Class use car fuction called ..???

class Vehicle(object):
    wheels = int(input(" W :"))
    def is_motorcycle(cls):
        return cls.wheels == 2
		
a = Vehicle()
print(a.is_motorcycle())



'''
output ==

4
4
VRooooommmm!
 W :2
True


4
4
VRooooommmm!
 W :5
False


'''