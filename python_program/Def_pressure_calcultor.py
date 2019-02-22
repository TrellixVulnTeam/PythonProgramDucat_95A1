# pressure calcultor use by def function ...????

def torr():
	t = float(input("enter the torr value : "))
	p = t / 133
	bar = p * (10**5)
	print("convert torr to pascal : ",p," pascal")
	print("convert torr to bar : ",bar," bar")

def bar():
	bar = float(input("enter the bar value : "))
	p = bar / (10**5)
	t = (133 * bar ) / (10**5)
	print("convert the bar to pasacl : ",p," pascal")
	print("convert the bar to torr : ",t," torr")
	
def pascal():
	p = float(input("enter the pascal value : "))
	bar = p * (10**5)
	t = 133 * p
	print("convert the pascal to bar : ",bar," bar")
	print("convert the pasacl to torr : ",t," torr")
	

print("torr , bar , pascal.")

choice = input("enter the user choice : ")

if choice == 'torr':
	torr()
	
elif choice == 'bar':
	bar()
	
elif choice == 'pascal':
	pascal()
	
else:
	print("invlid key.")
	
	
	
'''

output === 

torr , bar , pascal.
enter the user choice : pascal
enter the pascal value : 45698
convert the pascal to bar :  4569800000.0  bar
convert the pasacl to torr :  6077834.0  torr


torr , bar , pascal.
enter the user choice : torr
enter the torr value : 45
convert torr to pascal :  0.3383458646616541  pascal
convert torr to bar :  33834.58646616541  bar


torr , bar , pascal.
enter the user choice : bar
enter the bar value : 89745
convert the bar to pasacl :  0.89745  pascal
convert the bar to torr :  119.36085  torr



'''