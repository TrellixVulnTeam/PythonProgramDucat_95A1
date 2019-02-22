#154.   tally match project...??


n = int(input("enter the entries:"))
arr=[]
name_arr=[]
cls_arr=[]
mob_arr=[]
address_arr=[]
salary_arr=[]
for i in range(0,n):
    name = input("enter the name:")
    if len(name)<=15:
        print(name)
    else:
        print("maximum limit of charters.")
    cls = int(input("enter the class:"))
    if (cls>0 or cls<=12):
        print(cls)
    else:
        print("not found class.")
    mob = int(input("enter the mob.:"))
    if len(str(mob))<=10:
        print(mob)
    else:
        print("maximum no of mob.")
    address = input("enter the address:")
    if len(address)<=20:
        print(address)
    else:
        print("address lenght is not fully space.")
    salary = int(input("enter the salary:"))
    name_arr.append(name)
    cls_arr.append(cls)
    mob_arr.append(mob)
    address_arr.append(address)
    salary_arr.append(salary)
file = open("ram.txt","w")
file.write('NAME\tCLASS\tMOB\tADD\tSAL\n')
for j in range(n):
   file.write(name_arr[j]+ "\t" + str(cls_arr[j])+ "\t" + str(mob_arr[j])+ "\t" + address_arr[j]+ "\t" + str(salary_arr[j])+ "\n")
    # integer change in string then add the print statement ..??
  #   print(name_arr[j],cls_arr[j],mob_arr[j],address_arr[j],salary_arr[j])
file.close()
file = open("ram.txt","r")
file1 = open("shyam.txt","w")
while True:
    line= file.readline()
    if len(line)==0:
        break
    f=line.split('\t')
    a=','.join(f)
    file1.write(a)
file.close()
file1.close()
z= input("enter the search name:")
file1= open("shyam.txt","r")
while True:
    line= file1.readline()
    if len(line)==0:
        break
    x= line.split(',')
    if x[0]==z:
        print(x[0],x[1],x[2],x[3],x[4])
        break

file1.close()
