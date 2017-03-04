#Program to find second largest element in a sorted Array

def secondLargestElement(array):
	firstLargest=array[0]
	secondLargest=array[0]
	for x in range(1,len(array)):
		if array[x] >firstLargest:
			secondLargest=firstLargest
			firstLargest=array[x]
	return secondLargest

print secondLargestElement([1,3,4,5,6,9])