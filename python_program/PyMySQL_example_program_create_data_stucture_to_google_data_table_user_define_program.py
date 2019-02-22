# pyMySQL  ==   python + MySQL
'''
Command of MySQL  ==>>>
1*  $  user\saurabh\desktop > mySQL client command server

2*  open the cmd command mySQL ==>>    $    user\saurabh\desktop > mySql -u root -p

3*  $ user\saurabh\desktop\mySql > exit;                 #o/t ==  return to desktop  print with bye.

4*  $ user\saurabh\desktop\mysql  > create database google; # (any name user define)      #o/t  == create any data of the site .

5*  $ user\saurabh\desktop\mysql  > show databases;      # o/t == data show of the mysql 

6*  $ user\saurabh\desktop\mysql  > use google;          # o/t == database changed 

7*  $ user\saurabh\desktop\mysql  > create table client (id int(proxiy of input number # like that 5) primary key ,
      name varchar(50),age int ,amount int));            # o/t == quary ok, 0 rows data affected.

8*  $ user\saurabh\desktop\mysql  > show tables;

9*  $ user\saurabh\desktop\mysql  > desc client;         # o/t == describe data of client table of the any data.

10* $ user\saurabh\desktop\mysql  >  insert into client values (101,'Alex',45,45000);

11* $ user\saurabh\desktop\mysql  >  select * from client;

12* $ user\saurabh\desktop\mysql  > select name from client;

13* $ user\saurabh\desktop\mysql  > select name from client where id = 102;

14* $ user\saurabh\desktop\mysql  > select * from client where id = 102;

15* $ user\saurabh\desktop\mysql  > update client set name = 'Ram' where id = 102;

16* $ user\saurabh\desktop\mysql  > select * from client where id = 102;

17* $ user\saurabh\desktop\mysql  > delete from client where id = 102;

18* $ imp cammand of my sql to python combination file ......  $  desktop > pip install pyMySQL......

'''



from pymysql import *
con = connect(db="google",user="root",password="saurabh",host="localhost")
cur = con.cursor()
id1 = int(input("enter the client id : "))
name1 = input("enter the name : ")
age1 = int(input("enter the age : "))
ammount1 = float(input("enter the ammount : "))
query = """Insert into client (id,name,age,ammout) values (%s, %s, %s, %s)"""
tup = (id1,name1,age1,ammount1)
cur.execute(query,tup)
con.commit()
print("Record inserted.")
con.close()




'''
output ===


'''
