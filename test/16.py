def list_to_number(digits):

	strr = "".join(str(n) for n in digits)
	map(int , strr)
	return strr

print list_to_number([1,2,3])