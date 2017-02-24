#Occurence of given number in an Array

def countNumberOccurence(array,number):
	count=0
	for x in array:
		if x==number:
			count+=1
	return count
print countNumberOccurence([23,24,52,1,78,90,1],1)
