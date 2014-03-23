def count_words(arr):
	
	dic = {}
	for i in arr:
		if i in dic:
			dic[i] += 1
		else :
			dic[i] = 1	
	print dic
	print len(dic)

count_words(["da" , "ne" , "ivo e gei" , "da" , "ivo e gei"])

