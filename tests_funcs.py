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
		self.assertTrue(funcs.is_username_valid("abc"))
		self.assertTrue(funcs.is_username_valid("XYZ"))
		self.assertTrue(funcs.is_username_valid("Abc123"))

		self.assertFalse(funcs.is_username_valid("a"))
		self.assertFalse(funcs.is_username_valid("Abc-#"))
		self.assertFalse(funcs.is_username_valid("HtmlGoes<br>"))
		self.assertFalse(funcs.is_username_valid("\u00C8re"))  # \u00C8 = È

	def test_is_password_valid(self):
		self.assertTrue(funcs.is_password_valid("Abcdef#1"))
		self.assertTrue(funcs.is_password_valid("SecretPa§w0rδ"))
		self.assertTrue(funcs.is_password_valid("\u00C8É{_n00b"))  # \u00C8 = È

		self.assertFalse(funcs.is_password_valid("Abc#1"))
		self.assertFalse(funcs.is_password_valid("Abc123"))
		self.assertFalse(funcs.is_password_valid("Abc-#"))
		self.assertFalse(funcs.is_password_valid("HtmlGoes<br>"))

	def test_user_login(self):
		self.assertTrue(funcs.user_login(cursor, "Gerard", "éwi1épetits!"))
		self.assertTrue(funcs.user_login(cursor, "Bertrand", "M0t_De_passe"))
		self.assertTrue(funcs.user_login(cursor, "DestroyerDu75", "xXP@ssw0rdXx"))

		self.assertFalse(funcs.user_login(cursor, "Gerard", "ewi1épetits!"))
		self.assertFalse(funcs.user_login(cursor, "gerard", "éwi1épetits!"))
		self.assertFalse(funcs.user_login(cursor, "Neant", "jexistepa"))

	def test_user_create(self):
		funcs.user_create(cursor, "Username1", "@Password0")
		funcs.user_create(cursor, "NomUtilisateur", "1__Mdp__!")

		cursor.execute('SELECT username FROM `Users` WHERE username="Username1"')
		self.assertEqual(len(cursor.fetchall()), 1)

		cursor.execute('SELECT username FROM `Users` WHERE username="NomUtilisateur"')
		self.assertEqual(len(cursor.fetchall()), 1)

		# tester qu'il ne peut pas y avoir d'utilisateur en double
		funcs.user_create(cursor, "NomUtilisateur", "1__Mdp__!")
		cursor.execute('SELECT username FROM `Users` WHERE username="NomUtilisateur"')
		self.assertEqual(len(cursor.fetchall()), 1)

if __name__ == '__main__':
	conn = sqlite3.connect('test_database.db')
	cursor = conn.cursor()
	cursor.execute("DROP TABLE IF EXISTS `Users`")
	cursor.execute("""CREATE TABLE IF NOT EXISTS `Users` (
		`username` TEXT NOT NULL,
		`password` VARBINARY(32) NOT NULL,
		`spublickey` VARCHAR(128) NOT NULL,
		`sprivatekey` VARCHAR(128) NOT NULL,
		`epublickey` VARCHAR(128) NOT NULL,
		`eprivatekey` VARCHAR(128) NOT NULL
	)""")

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

	unittest.main()

	conn.commit()
	conn.close()
