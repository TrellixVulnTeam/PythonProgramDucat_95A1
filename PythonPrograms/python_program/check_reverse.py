# Python Program - Check Original Equals Reverse or Not


number = int(input("Enter any number: "))
orign = number
rev = 0
while number > 0:
    rev = (rev*10) + number%10;
    number = number//10
if orign == rev:
    print("Original number is equal to its reverse.")
else:
    print("Original number is not equal to its reverse.")
	
	
'''
output ==
Enter any number: 589
Original number is not equal to its reverse.
'''