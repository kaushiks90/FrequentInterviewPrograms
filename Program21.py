#Program To find the factorial of a number

def factorialofANumber(number):
	res=1
	for x in range(1,number+1):
		res=res*x
	return res
print factorialofANumber(5)


def factorialRecussive(number):
	if number==1:
		return 1
	return number*factorialRecussive(number-1)
print factorialRecussive(5)

