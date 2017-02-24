#Program to convert a number to binary number

def convertToBinary(number):
	binarynm=0
	pos=1
	while  number>0:
		rem=number%2
		binarynm=binarynm+(rem*pos)
		number=number//2
		pos=pos*10
	return binarynm
print convertToBinary(8)