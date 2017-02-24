#Program to count the digits of the string

def countdigitsInString(strings):
	count=0
	for x in strings:
		if x.isdigit():
			count+=1
	return count
print countdigitsInString("Kin34gs n45ver die56")