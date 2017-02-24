#Program to reverse a number

def reverseNumber(number):
	rem=0
	sum=0
	while  number>0:
		rem=number%10
		sum=(sum*10)+rem
		number=number//10
	return sum
print reverseNumber(123)
