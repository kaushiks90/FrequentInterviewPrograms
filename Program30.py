#Sum of Even / Odd Numbers in an Array
def sumOfEvenOddNumbers(array):
	even=0
	odd=0
	for x in range(0,len(array)):
		if(array[x]%2==0):
			even+=array[x]
		else:
			odd+=array[x]
	print "Even {} odd {}".format(even,odd)
sumOfEvenOddNumbers([3,6,1,2,9,0,7,4])