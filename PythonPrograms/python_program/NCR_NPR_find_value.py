#  Python Find ncR & nPr   ????

n = int(input("enter the nth term : " ))
r = int(input("enter the rth term : " ))
t = n - r

fact = 1
while n > 0:
	fact = fact * n
	n = n - 1
n_fact = fact
# print("n th term of fact value : ",n_fact)


fact1 = 1
while r > 0:
	fact1 = fact1 * r
	r = r - 1
r_fact = fact1
# print("r th term of fact value : ",r_fact)


fact2 = 1
while t > 0:
	fact2 = fact2 * t
	t = t - 1
diff_fact = fact2
# print("(n-r)th term of fact value : ",diff_fact)


NCR = ( n_fact ) // ( diff_fact *  r_fact )
print("total value of the given numbers its combination : ",NCR)


NPR = ( n_fact ) // ( diff_fact)
print("total value of the given numbers its permutation : ",NPR)


'''
output ===

enter the nth term : 10
enter the rth term : 7
total value of the given numbers its combination :  120
total value of the given numbers its permutation :  604800

'''