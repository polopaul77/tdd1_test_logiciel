import numpy as np

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
	s = 0
	for i in range(n):
		s += l[i]
	return s/n

def med_int(l):
	n = len(l)
	l.sort()
	if n%2:
		return l[n//2]
	else:
		return (l[n//2-1] + l[n//2])/2

def std_int(l):
	n = len(l)
	avg = avg_int(l)
	s = 0
	for i in range(n):
		s += np.square(l[i]-avg)
	return np.sqrt(s/n)