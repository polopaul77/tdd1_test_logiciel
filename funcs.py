def max_int(a,b):
	if a < b :
		return b
	else :
		return a

def min_int(a,b):
	if a < b :
		return a
	else :
		return b

def avg_int(l):
	n = len(l)
	sum = 0
	for i in range(n):
		sum += l[i]
	return sum/n
