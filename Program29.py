#Position of Given Number in an Array if the number is not found then print -1

def indexOfNumber(arrayInt,number):
	pos=-1
	for x in range(0,len(arrayInt)):
		if arrayInt[x]==number:
			pos=x+1
	return pos
print indexOfNumber([45,1,23,22,78,22],22)

