def count_vowels(string):
	
	strr = string.lower()
	count = 0
	for i in strr:
		if i == 'a' or i == 'e' or i == 'u' or i == 'o' or i =='y' or i =='i':
			count += 1
	return count

print count_vowels("Python")
print count_vowels("Theistareykjarbunga")