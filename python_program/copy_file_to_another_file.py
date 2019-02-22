# copy to file to another file data same copy to moves ....???

f = open("C:\\Users\\Saurabh\\Desktop\\file_handle\\file_write.txt","r")
g = open("C:\\Users\\Saurabh\\Desktop\\file_handle\\file_write1.txt","w")
a=f.read()
g.write(a)
g.seek(0)
print(a)
f.close()
g.close()