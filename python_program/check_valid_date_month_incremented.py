#21.  check valid date and incremented month or date .....???


n=input("enter the no:")
list= n.split("/")
dd=int(list[0])
mm=int(list[1])
yy=int(list[2])
if (mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    max=31
elif(mm==4 or mm==6 or mm==9 or mm==11):
    max=30
elif((yy%4==0 and yy%100!=0)or yy%400==0):
    max=29
else:
    max=28
if dd>max or dd<1:
    print("invalid")

elif mm>12 or mm<1:
    print("invalid")
else:
    print("valid")
    if (dd==max and mm!=12):       
        mm=mm+1
        dd=1
        print(dd, mm, yy)
    elif (dd==max and mm==12):       
        yy=yy+1
        mm=1
        dd=1
        print(dd,mm,yy)
    else:                               
        dd=dd+1
        print(dd,mm,yy)

		
		
'''
output  ===
**************************   another entry python ***************
enter the no:31/12/2018
valid
1 1 2019

**************************   another entry python ****************
enter the no:12/13/2019
invalid

'''