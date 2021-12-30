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

def med_int(l):
	n = len(l)
	l.sort()
	if n%2:
		return l[n//2]
	else:
		return (l[n//2-1] + l[n//2])/2
