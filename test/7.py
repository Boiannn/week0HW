def sevens_in_a_row(arr,n):
	counter = 0
	for i in range(0,len(arr)):
		if arr[i] == 7:
			counter += 1
			if counter == n:
				return True
		else:
			counter = 0
	return False

print sevens_in_a_row([1,7,1,7,7], 4)