from os import chdir,mkdir,rmdir,getcwd
chdir("F:/Python/py")
f=open('hello.txt','w')
f.close()
print(getcwd())
chdir("F:/Python")
rmdir("py")
print("Directry PY is Deleted")