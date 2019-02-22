# cars Trucks and bike all project use bye class project ...???

class Car():
    """A car for sale by Jeffco Car Dealership."""

    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'car'

a = Car()
print(a.vehicle_type())		
		
		
		
	
		
class Truck():
    """A truck for sale by Jeffco Car Dealership."""

    base_sale_price = 10000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'truck'

a = Truck()
print(a.vehicle_type())		
		
		
		
		
class Motorcycle():
    """A motorcycle for sale by Jeffco Car Dealership."""

    base_sale_price = 4000
    wheels = 2

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'motorcycle'
		
		
a = Motorcycle()
print(a.vehicle_type())


'''
output ===

car
truck
motorcycle



'''