def contains_digit(number , digit):
	if number < 0:
		number = abs(number)
	
	while number > 0:
		a = number%10

		if a == digit:
			return True

		number = number // 10
	return False

print contains_digit(12523, 5)
