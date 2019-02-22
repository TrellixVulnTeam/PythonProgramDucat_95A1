#148..   string read and append to any string in file:  ??

str= input('enter the string')
file= open("word.txt","a")
file.write(str)
file.close()
with open("word.txt","r") as file:
    print(file.read())
file.close()