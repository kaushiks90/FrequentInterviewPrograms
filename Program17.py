#Program to sort names descending in an Array

def sortNames(names):
	result=sorted(names,reverse=True)
	return result

array=["Ahi","Kln","zmn"]
print sortNames(array)