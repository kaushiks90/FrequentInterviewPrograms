#Count the number of Vowels in the given string
def countVowels(stringS):
	Vowels="aeiou"
	count=0
	for x in stringS:
		if x in Vowels:
			count+=1
	return count

print countVowels("KingsNeverDie")

