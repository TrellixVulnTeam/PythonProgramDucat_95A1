# **1***    Python Program to Merge Mails   ????



# Python program to mail merger
# Names are in the file names.txt
# Body of the mail is in body.txt

# open names.txt for reading
# with open("C:\Users\Saurabh\Desktop\names.txt",'r',encoding = 'utf-8') as names_file:


with open("C:\\Users\\Saurabh\\Desktop\\names.txt",'r',encoding = 'utf-8') as names_file:

   
	with open("C:\\Users\\Saurabh\\Desktop\\body.txt",'r',encoding = 'utf-8') as body_file:
   
        # read entire content of the body
		body = body_file.read()

        # iterate over names
		for name in names_file:
			mail = "Hello " + name + body

            # write the mails to individual files
			with open(name.strip()+".txt",'w') as mail_file:
				mail_file.write(mail)

			   
			      
			 
# **2***     Python Program to Find the Size (Resolution) of a Image   ?????



def jpeg_res(filename):
   """"This function prints the resolution of the jpeg image file passed into it"""

   # open image for reading in binary mode
   with open(filename,'rb') as img_file:

       # height of image (in 2 bytes) is at 164th position
       img_file.seek(163)

       # read the 2 bytes
       a = img_file.read(2)

       # calculate height
       height = (a[0] << 8) + a[1]

       # next 2 bytes is width
       a = img_file.read(2)

       # calculate width
       width = (a[0] << 8) + a[1]

   print("The resolution of the image is",width,"x",height)

jpeg_res("img1.jpg")





#  **3***     Python Program to Find Hash of File  ??????



# Python rogram to find the SHA-1 message digest of a file

# import hashlib module
import hashlib

def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

message = hash_file("track1.mp3")
print(message)


