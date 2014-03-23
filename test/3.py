def sum_of_min_and_max(arr):
	a = arr[0]
	b = arr[0]
	for i in range(0,len(arr)):

		if arr[i] < a:
			a = arr[i]
		elif arr[i] > b:
			b = arr[i]
	smm = a+b
	print smm
	return smm

sum_of_min_and_max([-10,5,10,100])