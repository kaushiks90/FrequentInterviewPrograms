#Find the number of words in a sentence

def totalWordsInSentence(stringS):
	tWordsCount=1
	for x in stringS:
		if x.isspace():
			tWordsCount+=1
	return tWordsCount

print totalWordsInSentence("Kings never die, fools die")