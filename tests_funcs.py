import funcs
import unittest
import sqlite3
from hashlib import md5
import string
import random

cursor = None

class TestFuncs(unittest.TestCase):

	def test_max_int(self):
		self.assertEqual(funcs.max_int(0,2),2)
		self.assertEqual(funcs.max_int(-1,-5),-1)
		self.assertEqual(funcs.max_int(-1,2),2)
		self.assertEqual(funcs.max_int(0,0),0)

	def test_is_username_valid(self):
		self.assertEqual(funcs.is_username_valid("abc"), True)
		self.assertEqual(funcs.is_username_valid("XYZ"), True)
		self.assertEqual(funcs.is_username_valid("Abc123"), True)
		self.assertEqual(funcs.is_username_valid("a"), False)
		self.assertEqual(funcs.is_username_valid("Abc-#"), False)
		self.assertEqual(funcs.is_username_valid("HtmlGoes<br>"), False)
		self.assertEqual(funcs.is_username_valid("\u00C8re"), False)  # \u00C8 = È

	def test_is_password_valid(self):
		self.assertEqual(funcs.is_password_valid("Abcdef#1"), True)
		self.assertEqual(funcs.is_password_valid("SecretPa§w0rδ"), True)
		self.assertEqual(funcs.is_password_valid("\u00C8É{_n00b"), True)  # \u00C8 = È
		self.assertEqual(funcs.is_password_valid("Abc#1"), False)
		self.assertEqual(funcs.is_password_valid("Abc123"), False)
		self.assertEqual(funcs.is_password_valid("Abc-#"), False)
		self.assertEqual(funcs.is_password_valid("HtmlGoes<br>"), False)

	def test_user_login(self):
		self.assertTrue(funcs.user_login(cursor, "Gerard", "éwi1épetits!"))
		self.assertTrue(funcs.user_login(cursor, "Bertrand", "M0t_De_passe"))
		self.assertTrue(funcs.user_login(cursor, "DestroyerDu75", "xXP@ssw0rdXx"))

		self.assertFalse(funcs.user_login(cursor, "Gerard", "ewi1épetits!"))
		self.assertFalse(funcs.user_login(cursor, "gerard", "éwi1épetits!"))
		self.assertFalse(funcs.user_login(cursor, "Neant", "jexistepa"))
		pass

if __name__ == '__main__':
	conn = sqlite3.connect('test_database.db')
	cursor = conn.cursor()
	cursor.execute("DROP TABLE IF EXISTS `Users`;")
	cursor.execute("""
		CREATE TABLE IF NOT EXISTS `Users` (
			`username` TEXT NOT NULL,
			`password` VARBINARY(32) NOT NULL,
			`spublickey` VARCHAR(128) NOT NULL,
			`sprivatekey` VARCHAR(128) NOT NULL,
			`epublickey` VARCHAR(128) NOT NULL,
			`eprivatekey` VARCHAR(128) NOT NULL
		);
	""")

	# remplir quelques utilisateurs arbitrairement
	users = [
		("Gerard", "éwi1épetits!"),
		("Bertrand", "M0t_De_passe"),
		("DestroyerDu75", "xXP@ssw0rdXx")
	]

	generate_key = lambda : ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(128))

	for username, password in users:
		md5_pass = md5(password.encode())
		keys = [generate_key() for i in range(4)]
		cursor.execute("INSERT INTO `Users` VALUES(?, ?, ?, ?, ?, ?)", [username, md5_pass.digest(), *keys])
		print("Inserted", username)

	unittest.main()

	conn.commit()
	conn.close()
