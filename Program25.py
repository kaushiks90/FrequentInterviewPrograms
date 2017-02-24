#Programs to count the vowels in the string

def countVowelsinString(stringS):
	count=0
	vowels="aeiou"
	for x in stringS:
		if x in vowels:
			count+=1
	return count

print countVowelsinString("Kings never die")

