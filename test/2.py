def sum_of_digits(n):
	if n < 0:
		n = abs(n)
	a = 0
	while n > 0:
		a += n%10
    	n = n // 10
	print a
	return a

sum_of_digits(123)