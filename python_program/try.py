# smith number ==  likes 378 ==>>  3+7+8=18       prime factor of 378 ====>>  2*3*3*3*7  == 2+3+3+3+7 == 18
# 378 is smith number its digit sum to equal to its number factor sum is equal to number is called the smith number ...??


def factors (n): 
	facts = [] 
	while True: 
		for f in range(2, n // 2 + 1): # 
			if n % f == 0: 
				facts.append(f) 
				n//= f 
				break 
			else: 
				facts.append(n) 
				break 
				return facts 

def sum_digits (n, sum = 0): 
	while n: 
		sum += n % 10 
		n //= 10 
		return sum 


num = int(input("Enter an integer: ")) 
num_sum = sum_digits(num) 
num_facts = factors(num) 
fact_sum = 0 
for f in num_facts: 
	fact_sum = sum_digits(f, fact_sum) 

print("Factors:", num_facts) 
print("Sum of digits:", num_sum) 
print("Sum of factors' digits:", fact_sum) 

if len(num_facts) == 1: 
	print("%d is prime (not a Smith Number)" % num) 
elif num_sum == fact_sum: 
	print("%d is a Smith Number" % num) 
else: 
	print("%d is not a Smith Number" % num) 