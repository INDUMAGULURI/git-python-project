import math
def isPerfectSquare(x):
	if(x >= 0):
		sr = math.sqrt(x)
		return ((sr*sr)==float(x))
	return false
x=int(input("Enter a number"))
if(isPerfectSquare(x)):
	print("Yes")
else:
	print("No")