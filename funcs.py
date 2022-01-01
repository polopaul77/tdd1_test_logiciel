import numpy as np
import random
import re
import string

from hashlib import md5
from typing import Tuple

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

def is_geo(l):
	n = len(l)
	if n == 1:
		return True
	else:
		try:
			q = l[1]/l[0]
		except ZeroDivisionError:
			q = 0

		for i in range(1,n):
			try:
				res = l[i]/l[i-1]
			except ZeroDivisionError:
				res = 0

			if res != q:
				return False

		return True

def is_ari(l):
	n = len(l)
	if n == 1:
		return True
	else:
		r = l[1] - l[0]

		for i in range(1,n):
			if l[i]-l[i-1] != r:
				return False

		return True

def geo_predict(n,l):
	if not is_geo(l):
		return [False, []]
	else:
		if n == 0:
			return [True, []]
		else:
			try:
				q = l[1]/l[0]
			except ZeroDivisionError:
				q = 0

			ll = [l[-1]*q]
			for i in range(1,n):
				ll.append(ll[i-1]*q)
			return [True, ll]

def ari_predict(n,l):
	if not is_ari(l):
		return [False, []]
	else:
		if n == 0:
			return [True, []]
		else:
			r = l[1] - l[0]

			ll = [l[-1] + r]
			for i in range(1,n):
				ll.append(ll[i-1]+r)
			return [True, ll]

username_regex = re.compile("([A-Za-z0-9]){4,}")
password_regex = re.compile("(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[^A-Za-z0-9]).{8,}")

def is_username_valid(username: str) -> bool:
	match = username_regex.match(username)
	return match is not None and match.group() == username

def is_password_valid(password: str) -> bool:
	match = password_regex.match(password)
	return match is not None and match.group() == password

def user_login(cursor, username: str, password: str) -> bool:
	md5_pass = md5(password.encode())
	cursor.execute("SELECT username FROM `Users` WHERE username=? AND password=?", [username, md5_pass.digest()])
	return len(cursor.fetchall()) > 0

def user_create(cursor, username: str, password: str):
	if is_username_valid(username) and is_password_valid(password):
		# check if username already exists or not
		cursor.execute("SELECT username FROM `Users` WHERE username=?", [username])
		if len(cursor.fetchall()) == 0:
			# create user and insert in database
			md5_pass = md5(password.encode())
			generate_key = lambda : ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(128))
			keys = [generate_key() for i in range(4)]
			cursor.execute("INSERT INTO `Users` VALUES(?, ?, ?, ?, ?, ?)", [username, md5_pass.digest(), *keys])

def user_get_keys(cursor, username: str) -> Tuple[str, str, str, str]:
	"""Il est supposé que username est un utilisateur existant et valide"""
	cursor.execute("SELECT spublickey, sprivatekey, epublickey, eprivatekey FROM `Users` WHERE username=?", [username])
	return cursor.fetchone()

def is_database_corrupted(cursor) -> bool:
	cursor.execute("SELECT * FROM `Users`")
	for username, password, spuk, sprk, epuk, eprk in cursor.fetchall():
		if not is_username_valid(username): return True
		if len(password) == 0: return True
		if len(spuk) < 128: return True
		if len(sprk) < 128: return True
		if len(epuk) < 128: return True
		if len(eprk) < 128: return True
	return False
