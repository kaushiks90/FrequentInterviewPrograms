#Program to count number of words in a string

def countNumberOfWords(strings):
	count=0
	for x in range(0,len(strings)):
		if strings[x].isspace():
			count+=1
	if len(strings)>0:
		return count+1
	else:
		return count

print countNumberOfWords("Kings Never Die")
