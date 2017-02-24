#Program to reverse an Array

def reverseAnArray(arraynum):
	for x in range(len(arraynum)-1,-1,-1):
		print arraynum[x]

reverseAnArray([56,3,45,12,89,34])


def reverseArrayMethod2(arraynum):
	limit=len(arraynum)/2
	totalSize=len(arraynum)
	for x in range(0,limit):
		temp=arraynum[x]
		arraynum[x]=arraynum[totalSize-1]
		arraynum[totalSize-1]=temp
		totalSize-=1
	print arraynum

reverseArrayMethod2([56,3,45,12,89,34])


