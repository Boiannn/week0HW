def is_an_bn(word):
	count = 0
	str(word)
	count = len(word)
	print count

	if count % 2 != 0:
		return False

	cnt = count / 2
	print cnt

	for i in range(0,len(word) - cnt):
		if i != 'a':
			return False

	for i in range(cnt,len(word)):
		if i != 'b':
			return False

	return True

print is_an_bn("aaabbb")
