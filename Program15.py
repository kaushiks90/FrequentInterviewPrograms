#Largest Absolute difference in an Array

def largestAbsDifference(array):
	ldiff=array[0]
	for x in range(1,len(array)-1):
		diff=abs(array[x]-array[x+1])
		if diff>ldiff:
			ldiff=diff
	return ldiff
print largestAbsDifference([5,8,2,5,-8])