#Program to count pairs whose Absoulte difference is 'D' (Given value) in an Array of integers

# Example arr=[10,3,5,7,2,8]

# d=2
# output 2 (10,5 and 7,2)

def countPairs(diffElement,*listInt):
	count=0
	result=[]
	for x in range(0,len(listInt)):
		for y in range(x,len(listInt)):
			if listInt[x]-listInt[y]==diffElement:
				count+=1
				result.append([listInt[x],listInt[y]])
	print result
	return count

print countPairs(5,10,3,5,7,2,8)
