#123.     New String  two list value where the First Character and the Last Character have been Exchanged.

def change(string):               # define change key.
    return string[-1:]+ string[1:-1]+ string[:1]      # modify key formula in any change (string)value..
m= input("enter the value:")
n= input("enter the value:")
print("modify string",change(string=m))
print("modify string",change(string=n))