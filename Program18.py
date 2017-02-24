#Find if the given number is a stepping number 

def isSteppingNumber(number):
	isSteppingNum=False
	prev_d=number%10
	number=number//10
	while  number!=0:
		cur_d=number%10
		if abs(prev_d-cur_d)!=1:
			isSteppingNum=False
			break
		else:
			prev_d=cur_d
			number=number//10
			isSteppingNum=True
	return isSteppingNum
print isSteppingNumber(321)


