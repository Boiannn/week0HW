def biggest_difference(arr):
	minn = arr[0]
	maxx = arr[0]
	
	for i in arr:
		if i < minn:
			minn = i
		elif i > maxx:
			maxx = i
	
	diff = minn - maxx
	
	return diff

print biggest_difference(range(100))