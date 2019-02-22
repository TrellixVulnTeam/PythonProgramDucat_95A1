# file replace is to was in any file ..???
f = open("C:\\Users\\Saurabh\\Desktop\\file_handle\\filereplace.txt","r")
a=f.read()
print(a)
b = input("enter the world: ")
c = input("enter the world replace :")
a=a.replace(b,c)
print(a)






# new file ...??

f = open("C:\\Users\\Saurabh\\Desktop\\file_handle\\filereplace.txt","r")
a=f.read()
print(a)
a=a.replace(' is ',' was ')
print(a)


# new file ...??

f = open("C:\\Users\\Saurabh\\Desktop\\file_handle\\filereplace.txt","w")
w = input("enter the user data : ")
f.write(w)
f.seek(0)
a=f.read()
print(a)
a=a.replace(' is ',' was ')
print(a)