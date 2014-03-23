def count_substrings(haystack,needle):
	count = 0
	k = len(needle)
	tru = False
	for i in haystack:
		if i = needle[0]:
			while k>1:
				i+= 1
				if i == needle[i]:
					tru = True
			if tru == True:
				count += 1
	return count

print count_substrings("This is a test string", "is")

