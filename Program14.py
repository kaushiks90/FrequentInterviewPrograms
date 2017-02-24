#Sum of both the diagonal in a matrix

def printSumOfDiagonal(m):
	sum=0
	if len(m)==len(m[0]):
		for x in range(0,len(m)):
			for y in range(x,len(m)):
				if x==y:
					sum+=m[y][y]
			for z in range(0,len(m)):
				if x+z==len(m)-1:
					#print m[x][y]
					sum+=m[x][z]
	return sum


print printSumOfDiagonal([[1,2,3],[4,5,6],[7,8,9]])
