#Count occurence of given character in a string 

def findOccurence(strings,searchch):
	count=0
	for x in strings:
		if x==searchch:
			count+=1
	return count

print findOccurence("kings never die",'e')
