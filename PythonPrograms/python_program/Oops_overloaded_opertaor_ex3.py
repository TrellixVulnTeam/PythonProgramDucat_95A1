#  overlload_+_operator3.py   oprator BY oops and class ....??


class Sample:
    def __init__(self,x):
        self.x=x
    def __truediv__(self,other):
        m=self.x + other.x
        return m
obj1=Sample(100)
obj2=Sample(200)
#print(obj1.__truediv__(obj2))	
print(obj1/obj2)




'''
output ===

300
but user choice the __truediv__   is call the add mathod fuction ....???
not divide to add value of function .

'''