def prepare_meal(number):
	saven = number
	n = 0
	yeah = ''
	while number > 1:
		if number % 3 == 0:
			n += 1
			number = number / 3
		else: 
			break
	
	for i in range(0,n):
		yeah += 'spam' + ' '

	if saven % 5 == 0:
		yeah += 'and eggs'

	return yeah

print prepare_meal(45)

