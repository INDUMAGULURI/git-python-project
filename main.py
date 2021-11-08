n=int(input("Enter a number:"))
def check_palindrome(str1):
	if(str1[::-1]==str1):
		return True
if(check_palindrome(str)==True):
	print("Palindrome")
else:
	print("Not palindrome")