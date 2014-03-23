def prime_number_of_divisors(n):
	divisors = 0
	for i in range(1,n+1):
		if n%i == 0:
			divisors += 1
	return divisors

def is_prime(n):
	if n < 0:
		n = abs(n)

	prime = True

	for i in range(2,n):
		if  n%i == 0:
			prime = False
			return prime
	return prime	



print is_prime(prime_number_of_divisors(8))		