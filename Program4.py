#Program to Find the Count of Sorted Rows in a Matrix
def checkSortedRowsInMatrix(array):
	for x in array:
		for y in x:
			z= y-1
