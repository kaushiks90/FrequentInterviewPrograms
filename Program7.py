#Find the number of letter in the given sentence excluding spaces

print dir(str)
def lettersinSentence(stringS):
	count=0
	for x in stringS:
		if x.isalpha():
			count+=1
	return count

print lettersinSentence("Kings 8977 never di34")
