# star pattern in diamond shape ...??

for i in range(1,6):
	for j in range(1,6-i):
		print("  ",end=" ")
	for j in range(1,i+1):
		print("*_",end=" ")
	print()
for i in range(4,0,-1):
	for j in range(1,6-i):
		print("  ",end=" ")
	for j in range(1,i+1):
		print("*_",end=" ")
	print()
	
	
'''
            *_
         *_ *_
      *_ *_ *_
   *_ *_ *_ *_
*_ *_ *_ *_ *_
   *_ *_ *_ *_
      *_ *_ *_
         *_ *_
            *_
'''




for i in range(1,6):
	for j in range(1,6-i):
		print(" ",end=" ")
	for j in range(1,i+1):
		print("_*_",end=" ")
	print()
for i in range(4,0,-1):
	for j in range(1,6-i):
		print(" ",end=" ")
	for j in range(1,i+1):
		print("_*_",end=" ")
	print()
	
	
'''
        _*_
      _*_ _*_
    _*_ _*_ _*_
  _*_ _*_ _*_ _*_
_*_ _*_ _*_ _*_ _*_
  _*_ _*_ _*_ _*_
    _*_ _*_ _*_
      _*_ _*_
        _*_

'''



for i in range(1,6):
	for j in range(1,6-i):
		print("  ",end=" ")
	for j in range(1,i+1):
		print("* ",end=" ")
	print()
for i in range(4,0,-1):
	for j in range(1,6-i):
		print("  ",end=" ")
	for j in range(1,i+1):
		print("* ",end=" ")
	print()
	
	
'''
            *
         *  *
      *  *  *
   *  *  *  *
*  *  *  *  *
   *  *  *  *
      *  *  *
         *  *
            *

'''



for i in range(1,6):
	for j in range(1,6-i):
		print(" ",end=" ")
	for j in range(1,2*i):
		print("*",end=" ")
	print()
for i in range(4,0,-1):
	for j in range(1,6-i):
		print(" ",end=" ")
	for j in range(1,2*i):
		print("*",end=" ")
	print()
	
	
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

'''
