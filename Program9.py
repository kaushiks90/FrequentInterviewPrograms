#Check if a given number is a palindrome

def reverseNum(number):
	rem=0
	sum=0
	while number!=0:
		rem=number%10
		sum=(sum*10)+rem
		number=number//10
	return sum


def isNumberPalindrome(number):
	reversedNumber=reverseNum(number)
	if number==reversedNumber:
		return True
	else:
		return False

print isNumberPalindrome(343)


