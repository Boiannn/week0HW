def nth_fibonacci(n):
	first = 1
	second = 1
	if n == 1 or n == 2:
		return 1
	elif n > 2:
		for i in range(2,n):
			n = first + second
			first = second
			second = n

		return n
print nth_fibonacci(10)