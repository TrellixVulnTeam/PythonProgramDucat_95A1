# overlload_get_item_equal_operator.py   by Oops and class ..??

class Sample:
    def __init__(self,x):
        self.x=x	
    def __le__(self,other):	
        if(self.x>=other.x): 
            return 1	
        else:
            return 0
obj1=Sample(100)
obj2=Sample(10)   
if(obj1<=obj2):	
    print("obj1 is smaller or Equal to obj2")
else:
    print("obj2 is smaller")

	
	
	
'''
output ==

obj1 is smaller or Equal to obj2

'''