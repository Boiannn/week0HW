def contains_digit(number , digit):
	if number < 0:
		number = abs(number)
	
	while number > 0:
		a = number%10

		if a == digit:
			return True

		number = number // 10
	return False



def contains_digits(number , digits):

	for i in digits:
		truth = contains_digit(number , i)
		if truth == False:
			return False
	return True

print contains_digits(402123, [0, 3, 4])

