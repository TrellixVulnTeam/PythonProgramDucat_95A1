# finally excute on the last always .  but print last then program has excuted then print not ? and finally always print in last excute pragram ..??


try:
	a= int(input("enter the A: "))
	b= int(input("eneter the B: "))
	print(a/b)
	print("Division is complete.")
except ZeroDivisionError as Z:
	print(Z)
except ValueError as V:
	print(V)
finally:
	print("thank you.")



'''
output ==


enter the A: 5
eneter the B: 4
1.25
Division is complete.
thank you.


enter the A: 5
eneter the B: 0
division by zero
thank you.


enter the A: thank you.
Traceback (most recent call last):
  File "Finally_excute_inFileError.py", line 5, in <module>
    a= int(input("enter the A: "))
KeyboardInterrupt


'''

