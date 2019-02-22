# Python Program - List All Files in Directory
		
import glob, os
os.chdir("C:/Python34")
for file in glob.glob("*.*"):
    print(file)