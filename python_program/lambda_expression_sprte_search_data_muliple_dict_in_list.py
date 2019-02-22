# search any data of the given point in lambda expression so given the values of the fuction print mltiple dict in list sprate to each search data user input ..???

a = [{'name':'ram','class':'python','batch timing': '8am','points':8},
		{'name':'shyam','class':'python','batch timing': '9am','points':9},
		{'name':'sita','class':'java','batch timing': '9am','points':8},
		{'name':'saurabh','class':'python','batch timing': '8am','points':10},
		{'name':'rishabh','class':'jsnode4','batch timing': '8am','points':8},
	]
	
print(list(filter(lambda x : x['points']==8,a)))
print(list(filter(lambda x : x['class']=='python',a)))



'''
output ==

[{'name': 'ram', 'class': 'python', 'batch timing': '8am', 'points': 8},
 {'name': 'sita', 'class': 'java', 'batch timing': '9am', 'points': 8},
 {'name': 'rishabh', 'class': 'jsnode4', 'batch timing': '8am', 'points': 8}]
 
[{'name': 'ram', 'class': 'python', 'batch timing': '8am', 'points': 8},
 {'name': 'shyam', 'class': 'python', 'batch timing': '9am', 'points': 9},
 {'name': 'saurabh', 'class': 'python', 'batch timing': '8am', 'points': 10}]
 
 
'''