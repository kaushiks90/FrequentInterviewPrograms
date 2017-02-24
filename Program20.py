#Find the greates of three numbers

def greatestOfThreeNumbers(num1,num2,num3):
	if num1>num2 and num2>num3:
		print "Number 1 is greatest",num1
	elif num2>num3:
		print "Number 2 is greatest",num2
	else:
		print "Number 3 is greatest",num3
greatestOfThreeNumbers(1,2,9)