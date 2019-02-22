# time calcultor used by def_ function ....????

def sec():
	s = float(input("enter the sec. : "))
	mcs = s * (10**6)
	mls = s * (1000)
	min = s / (60)
	hour = s / 3600
	day =  s / (3600 * 24)
	week = s / (3600 * 24 * 7)
	month = s / (3600 * 24 * 7 * 31)
	year = s / (3600 * 24 * 7 * 365)
	print("chnage second to microsecond : ",mcs)
	print("chnage second to milisecond : ",mls)
	print("chnage second to min : ",min)
	print("chnage second to hour : ",hour)
	print("chnage second to day : ",day)
	print("chnage second to week : ",week)
	print("chnage second to month : ",month)
	print("chnage second to year : ",year)
	
def min():
	m = float(input("enter the min. : "))
	mcs = m * 60 * (10**6)
	mls = m * 60 * (1000)
	sec = m * (60)
	hour = m / 60
	day =  m / (60 * 24)
	week = m / (60 * 24 * 7)
	month = m / (60 * 24 * 7 * 31)
	year = m / (60 * 24 * 7 * 365)
	print("chnage min to microsecond : ",mcs)
	print("chnage min to milisecond : ",mls)
	print("chnage min to sec : ",sec)
	print("chnage min to hour : ",hour)
	print("chnage min to day : ",day)
	print("chnage min to week : ",week)
	print("change min to month : ",month)
	print("chnage min to year : ",year)
	
def hour():
	h = float(input("enter the hour : "))
	mcs = h * 3600 * (10**6)
	mls = h * 3600 * (1000)
	sec = h * (3600)
	min = h / 60
	day =  h / ( 24)
	week = h / ( 24 * 7)
	month = h / (24 * 7 * 31)
	year = h / ( 24 * 7 * 365)
	print("chnage hour to microsecond : ",mcs)
	print("chnage hour to milisecond : ",mls)
	print("chnage hour to min : ",sec)
	print("chnage hour to min : ",min)
	print("chnage hour to day : ",day)
	print("chnage hour to week : ",week)
	print("chnage hour to year : ",year)
	
def year():
	y = float(input("enter the year : "))
	mcs = y * (24 * 7 * 365 * 60 * 60 * (10**9))
	mls = y * (24 * 7 * 365 * 60 * 60 * (10**3))
	sec = y * (24 * 7 * 365 * 60 * 60 )
	min = y * (24 * 7 * 365 * 60 )
	hour = y * (24 * 7 * 365 )
	day = y * (365 )
	month = y * ( 12 )
	week = y * (52.14)
	print("year to mcs : ",mcs)
	print("year to mls : ",mls)
	print("year to sec : ",sec)
	print("year to min : ", min )
	print("year to hour : ", hour)
	print("year to day : ",day)
	print("year to week : ",week)
	print("year to month : ",month)
	
print("sec , min ,hour ,year .")

choice = input("enter the user choice : ")

if choice == 'sec':
	sec()
	
elif choice == 'min':
	min()
	
elif choice == 'hour':
	hour()
	
elif choice == 'year':
	year()
	
else:
	print("invalid key.")
	
	
'''
output ===


sec , min ,hour ,year .
enter the user choice : hour
enter the hour : 24
chnage hour to microsecond :  86400000000.0
chnage hour to milisecond :  86400000.0
chnage hour to min :  86400.0
chnage hour to min :  0.4
chnage hour to day :  1.0
chnage hour to week :  0.14285714285714285
chnage hour to year :  0.0003913894324853229


sec , min ,hour ,year .
enter the user choice : year
enter the year : 12
year to mcs :  2.649024e+18
year to mls :  2649024000000.0
year to sec :  2649024000.0
year to min :  44150400.0
year to hour :  735840.0
year to day :  4380.0
year to week :  625.6800000000001
year to month :  144.0


sec , min ,hour ,year .
enter the user choice : sec
enter the sec. : 1546987654897546987459644
chnage second to microsecond :  1.546987654897547e+30
chnage second to milisecond :  1.5469876548975468e+27
chnage second to min :  2.578312758162578e+22
chnage second to hour :  4.2971879302709635e+20
chnage second to day :  1.7904949709462348e+19
chnage second to week :  2.557849958494621e+18
chnage second to month :  8.251128898369746e+16
chnage second to year :  7007808105464716.0



'''