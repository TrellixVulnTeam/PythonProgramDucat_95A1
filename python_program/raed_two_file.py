# read two file in the given file ....???

f = open('C:/Users/Saurabh/Desktop/file_handle/sample.txt','r')
a = f.read()
print(a)
f.close()

'''
output ====

To give you a personalized experience,
 your language and location settings will help us determine the content you see.
 Please be aware, some content may not be available in all languages.
 By using our website you consent to all cookies in
 
'''

f = open('C:/Users/Saurabh/Desktop/file_handle/sample.txt','r')
a = f.read()
print(a)
b = f.read()
print(b)
f.close()

'''
output ====
To give you a personalized experience,
 your language and location settings will help us determine the content you see.
 Please be aware, some content may not be available in all languages.
 By using our website you consent to all cookies in
 
'''

f = open('C:/Users/Saurabh/Desktop/file_handle/sample.txt','r')
a = f.read(15)
print(a)
f.close()

# we can read file and ans to only 15 char print in cmd output ...???
# output =====     To give you a p



'''
print one time f.close() is read only one time then exit the program so we can write the program only one time read...????
use the seek mathod we can use the value of mathod again run to next to next time then read again for user given value after the value can 
# f.seek(uservalue..... likethat  6,1,2....)
'''

f = open('C:/Users/Saurabh/Desktop/file_handle/sample.txt','r')
a = f.read()
f.seek(0)     # use file.seek(given value file read again to again the value has read the file of contents again read and write to run program in any file.)
print(a)
b = f.read()
print(b)
f.close()



'''
output ==

To give you a personalized experience,
 your language and location settings will help us determine the content you see.
 Please be aware, some content may not be available in all languages.
 By using our website you consent to all cookies in
 
To give you a personalized experience,
 your language and location settings will help us determine the content you see.
 Please be aware, some content may not be available in all languages.
 By using our website you consent to all cookies in

'''