#7. five subject mark in user input find the result and grade both using by conditions..??

hindi= int(input("enter the mark of hindi:"))
english = int(input("enter the mark of english:"))
physics = int(input("enter the mark of physics:"))
chemistry = int(input("enter the mark of chemistry:"))
maths = int(input("enter the mark of maths:"))
result = (hindi+english+physics+chemistry+maths)/5
print(result)
if (result>0 and result<33):
    print("fail\nf grade.")
elif (result >=33  and result < 45):
    print("pass\ne grade.")
elif (result>=45 and result<60):
    print("pass\nd grade.")
elif (result>=60 and result<70):
    print("pass\nc grade.")
elif(result>=70 and result<80):
    print("pass\nb grade.")
elif(result>=80 and result<90):
    print("pass\na grade.")
elif(result<=100):
    print("pass\ns grade.")
else:
    print("invalid result.")
