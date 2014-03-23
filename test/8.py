def is_int_palindrom(n):

	if n < 0 :
		n = abs(n)

	rev = ""

	strr = str(n)

	for i in strr:
		rev = i + rev

	if rev == str(n):
		return True			
		
	return False

print is_int_palindrom(12321)




