#Prime Factors of a given number
def isXPrime(z):
	for y in range(3,z+1):
		if z %y==0:
			return y
		else:
			continue

def primeFactorsOfNumber(number):
	res=0
	listPrimeFactors=[]
	while number%2==0:
		listPrimeFactors.append(2)
		number=number//2
	while number!=1:
		res=isXPrime(number)
		if res!=0 and number%res==0:
		 	listPrimeFactors.append(res)
		 	number=number//res
	print listPrimeFactors
primeFactorsOfNumber(315)

