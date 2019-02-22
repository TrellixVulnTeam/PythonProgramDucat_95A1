# (w+)    file write on the read of the file to overlap on the file word charter to how many right down on the way how many char on overlap and 
#  same print previous file text.. 



f = open("C:\\Users\\Saurabh\\Desktop\\file_handle\\lenstring.cpp","w+")
f.write("hello python world in the ducat work in the lab.")
f.seek(0)
print(f.read())
print("file created.")
f.close()


'''
output ==

hello python world in the ducat work in the lab.
file created.

'''