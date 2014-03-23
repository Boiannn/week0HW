def count_consonants(string):
	
	strr = string.lower()
	count = len(string)
	for i in strr:
		if i == 'a' or i == 'e' or i == 'u' or i == 'o' or i =='y' or i =='i':
			count -= 1
	return count

print count_consonants("Python")