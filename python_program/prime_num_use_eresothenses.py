#19.  print all print number using eresothenses (chlni) mathod .>>>


n=int(input("enter the no:"))
for i in range (2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)