#89.  find the gravitetional force in given two object of form f=Gm1m2/r**2

m1=int(input("enter the 1st object  mass:"))
m2=int(input("enter the 2nd object  mass:"))
r=int(input('enter the radius of object:'))
G= 6.67*(10**(-11))             # put tha value of G.
f= ( G*m1*m2/(r**2))            # formula of gravitatinal force :...>>
print("the gravitational force of two object F = Gm1m2/r**2 = ",f)