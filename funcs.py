import re

def max_int(a,b):
	if a < b :
		return b
	else :
		return a


username_regex = re.compile("([A-Za-z0-9]){4,}")
password_regex = re.compile("(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[^A-Za-z0-9]).{8,}")

def is_username_valid(username: str) -> bool:
	match = username_regex.match(username)
	return match is not None and match.group() == username

def is_password_valid(password: str) -> bool:
	match = password_regex.match(password)
	return match is not None and match.group() == password

def user_login(cursor, username: str, password: str) -> bool:
	return None

def user_create(cursor, username: str, password: str):
	pass
