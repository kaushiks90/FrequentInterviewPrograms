#Program to Find Sum of opposite Diagonal Elements of a Matrix

def printSumOfDiagonal(m):
	sum=0
	if len(m)==len(m[0]):
		for x in range(0,len(m)):
			for y in range(0,len(m)):
				if x+y==len(m)-1:
					#print m[x][y]
					sum+=m[x][y]
	return sum


print printSumOfDiagonal([[1,2,3],[4,5,6],[7,8,9]])
