#  file handle in file error in handle to data as to go as handle plz..??


try:
	f=open("c:/file/intro.txt","r")
	s=f.read()
	print(s)
	f.close()
except FileNotFoundError as f:
	print(f)
	
	
	

	
	
'''
output ==

[Errno 2] No such file or directory: 'c:/file/intro.txt'

'''
	
	