#Given a string containing just characters '(' ')' [  ] and the given string in the string 
# Valid -() ()[]{} {}{(){}} {([])}
#Invalid -(]) ([)]) {(}}} {[(])]}

#print dir(list)

def ifParenthesisMatching(bracOpen,bracClose):
	if bracOpen=='(' and bracClose==')':
		return True
	if bracOpen=='{' and bracClose=='}':
		return True
	if bracOpen=='[' and bracClose==']':
		return True


def booleanIsvalid(stringS):
	OPenB="([{"
	CloseB="}])"
	stack=[]
	result=False
	for x in stringS:
		if x in OPenB:
			stack.append(x)
		if x in CloseB:
			if len(stack)>0 and ifParenthesisMatching(stack.pop(),x):
				result=True
			else:
				result=False
				break
	return result

print booleanIsvalid("({})")
print booleanIsvalid("[[[]){}")
