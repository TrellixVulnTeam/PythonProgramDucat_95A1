#87.    filehandle ..??

filehandle = open("D:\\message.txt","w")
txt= "NAME   \tsalary \nsaurabh ganguly   \t2500   \nSandeep chaturvedi   \t5000   \nrabina   \t7500   \nnaager   \t10000."
filehandle.write(txt)
filehandle.close()

filehandle = open("message.txt","a")
print(filehandle.read())
filehandle.close()