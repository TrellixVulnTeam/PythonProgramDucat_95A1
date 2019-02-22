#126.    print all number in with used loop in range value (1,upper) :...??

def printno(upper):      # define the upper key:
    if(upper>0):           # condition of the upper is greater to 0.
        printno(upper-1)       # less 1 in no print on screen .
        print(upper)
upper= int(input("enter the upper limit number:"))
printno(upper)                 # print numbers.