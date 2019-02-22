try:
    f=open("C:/sers/Dell/Deskto/python 6 week/Python/file/intro.txt","r")
    s=f.read()
    print(s)
    f.close()
except:
    print("File Not Found")
