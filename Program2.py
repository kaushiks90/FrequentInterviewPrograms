#Program to Find the Count of Occurrences of Each Character in a String
#"PROGRAMMING" P=1 R=2 O=1 G=2 M=2 I=1 N=1 A=1
def countOccurence(srtingS):
	dictCount={}
	for x in srtingS:
		if x not in dictCount:
			dictCount.update({x:1})
		else:
			value=dictCount[x]
			dictCount[x]=value+1
	print dictCount
countOccurence("PROGRAMMING")
