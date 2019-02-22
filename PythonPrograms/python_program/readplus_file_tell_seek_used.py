# read plus file and searching to moves cursor location and carry to 0th postion ...??


f = open("C:\\Users\\Saurabh\\Desktop\\file_handle\\lenstring.cpp","r+")
f.write("hello python world in the ducat work in the lab.")
f.seek(0)                           # location carry to moves on the 0 th place otherwise user choice .
print(f.read())
print("file created.")
print(f.tell())                     #  location of searching the cursor moves which places value of the position. 
f.close()



'''
output ====
hello python world in the ducat work in the lab.
file created.
48

'''


f = open("C:\\Users\\Saurabh\\Desktop\\file_handle\\lenstring.cpp","r+")
f.write("MYSQL")       
f.close()


'''
output ===

'''