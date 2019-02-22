#   file read to another path and we can store in any value then use the all charcter count to another file ...????
# path define the file is change to backsalce to forword slace .. ('\' (backword slace)  ==   '/' (forword slace))


f=open("C:/Users/Saurabh/Desktop/file_handle/railway.txt","r")
str=f.read()
lv = 0
lc = 0
uv = 0
uc = 0
d = 0
s = 0
sp = 0
for i in str:
	if (ord(i)>=97 and ord(i)<=122):
		if (ord(i)==97 or ord(i)==101 or ord(i)==105 or ord(i)==111 or ord(i)==117):
			lv = lv+1
		else:
			lc = lc+1
	elif (ord(i)>=65 and ord(i)<=90):
		if (ord(i)==65 or ord(i)==69 or ord(i)==73 or ord(i)==79 or ord(i)==85):
			uv = uv+1
		else:
			uc = uc+1
	elif (ord(i)>=48 and ord(i)<=57):
		d = d+1
	elif (ord(i)==32):
		s = s+1
	else:
		sp = sp+1
		
print("lowercase vowel      : ",lv)
print("lowercase consonents : ",lc)
print("uppercase vowel      : ",uv)
print("uppercase consonents : ",uc)
print("digit                : ",d)
print("space                : ",s)
print("spacial charcter     : ",sp)



'''
output ====

lowercase vowel      :  269
lowercase consonents :  416
uppercase vowel      :  7
uppercase consonents :  16
digit                :  16
space                :  131
spacial charcter     :  33

'''