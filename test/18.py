def slope_style_score(scores):
	minn = scores[0]
	maxx = scores[0]
	summ = 0
	for i in scores:
		if i < minn:
			minn = i
		elif i > maxx:
			maxx = i

	for i in scores:
		summ += i

	summ = summ - maxx - minn
	summ = float(summ / (len(scores) - 2))
	return summ

