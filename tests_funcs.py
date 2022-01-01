import numpy as np
import funcs
import random
import sqlite3
import string
import unittest

from hashlib import md5

cursor = None

class TestFuncs(unittest.TestCase):

	def test_max_int(self):
		self.assertEqual(funcs.max_int(0,2),2)
		self.assertEqual(funcs.max_int(-1,-5),-1)
		self.assertEqual(funcs.max_int(-1,2),2)
		self.assertEqual(funcs.max_int(0,0),0)

	def test_min_int(self):
		self.assertEqual(funcs.min_int(0,4),0)
		self.assertEqual(funcs.min_int(-1,-7),-7)
		self.assertEqual(funcs.min_int(-5,5),-5)
		self.assertEqual(funcs.min_int(3,3),3)
		self.assertEqual(funcs.min_int(-5,-5),-5)

	def test_avg_int(self):
		self.assertEqual(funcs.avg_int([1,2,3,4,5]),3)
		self.assertEqual(funcs.avg_int([-2,-4]),-3)
		self.assertEqual(funcs.avg_int([-2,-1,1,2]),0)
		self.assertEqual(funcs.avg_int([0,0,0,0,0]),0)
		self.assertEqual(funcs.avg_int([13]),13)

	def test_med_int(self):
		self.assertEqual(funcs.med_int([4,2,5,1,2]),2)
		self.assertEqual(funcs.med_int([1,10]),5.5)
		self.assertEqual(funcs.med_int([-2,1,10,1]),1)
		self.assertEqual(funcs.med_int([0,0,0,0,0]),0)
		self.assertEqual(funcs.med_int([13]),13)

	def test_std_int(self):
		self.assertEqual(funcs.std_int([1,2,3,4,5]),np.sqrt(2))
		self.assertEqual(funcs.std_int([1,10]),4.5)
		self.assertEqual(funcs.std_int([-2,1,10,1]),4.5)
		self.assertEqual(funcs.std_int([0,0,0,0,0]),0)
		self.assertEqual(funcs.std_int([13]),0)

	def test_is_geo(self):
		self.assertEqual(funcs.is_geo([5,10,20,40,80]), True)
		self.assertEqual(funcs.is_geo([2,1,0.5,0.25,0.125]), True)
		self.assertEqual(funcs.is_geo([0,0,0,0]), True)
		self.assertEqual(funcs.is_geo([4,-4,4,-4]), True)
		self.assertEqual(funcs.is_geo([1,2,3,4]), False)
		self.assertEqual(funcs.is_geo([-6,-9,7,1,-1,0]), False)
		self.assertEqual(funcs.is_geo([2,6,18,4]), False)

	def test_is_ari(self):
		self.assertEqual(funcs.is_ari([3,5,7,9,11,13]), True)
		self.assertEqual(funcs.is_ari([10,5,0,-5,-10,-15]), True)
		self.assertEqual(funcs.is_ari([0,0,0,0]), True)
		self.assertEqual(funcs.is_ari([4,-4,4,-4]), False)
		self.assertEqual(funcs.is_ari([1,2,4,8,16]), False)

	def test_geo_predict(self):
		self.assertEqual(funcs.geo_predict(3, [5,10,20,40,80]), [True, [160,320,640]])
		self.assertEqual(funcs.geo_predict(1, [2,1,0.5,0.25,0.125]), [True, [0.0625]])
		self.assertEqual(funcs.geo_predict(0, [1,2,4,8,16]), [True, []])
		self.assertEqual(funcs.geo_predict(4, [0,0,0,0]), [True, [0,0,0,0]])
		self.assertEqual(funcs.geo_predict(2, [4,-4,4,-4]), [True, [4,-4]])
		self.assertEqual(funcs.geo_predict(4, [1,2,3,4]), [False, []])
		self.assertEqual(funcs.geo_predict(2, [-6,-9,7,1,-1,0]), [False, []])
		self.assertEqual(funcs.geo_predict(0, [2,6,18,4]), [False, []])

	def test_ari_predict(self):
		self.assertEqual(funcs.ari_predict(3, [3,5,7,9,11,13]), [True, [15,17,19]])
		self.assertEqual(funcs.ari_predict(1, [10,5,0,-5,-10,-15]), [True, [-20]])
		self.assertEqual(funcs.ari_predict(0, [1,1.5,2]), [True, []])
		self.assertEqual(funcs.ari_predict(2, [0,0,0,0]), [True, [0,0]])
		self.assertEqual(funcs.ari_predict(3, [4,-4,4,-4]), [False, []])
		self.assertEqual(funcs.ari_predict(5, [1,2,4,8,16]), [False, []])

	def test_is_username_valid(self):
		self.assertTrue(funcs.is_username_valid("abcd"))
		self.assertTrue(funcs.is_username_valid("WXYZ"))
		self.assertTrue(funcs.is_username_valid("Abc123"))

		self.assertFalse(funcs.is_username_valid("a"))
		self.assertFalse(funcs.is_username_valid("Abc-#"))
		self.assertFalse(funcs.is_username_valid("HtmlGoes<br>"))
		self.assertFalse(funcs.is_username_valid("\u00C8re"))  # \u00C8 = È

	def test_is_password_valid(self):
		self.assertTrue(funcs.is_password_valid("Abcdef#1"))
		self.assertTrue(funcs.is_password_valid("SecretPa§w0rδ"))
		self.assertTrue(funcs.is_password_valid("\u00C8ÉE{_n00b"))  # \u00C8 = È
		self.assertTrue(funcs.is_password_valid("1PassSecretδ"))

		self.assertFalse(funcs.is_password_valid("Abc#1"))
		self.assertFalse(funcs.is_password_valid("Abc123"))
		self.assertFalse(funcs.is_password_valid("Abc-#"))
		self.assertFalse(funcs.is_password_valid("HtmlGoes<br>"))
		self.assertFalse(funcs.is_password_valid("SPEACSRSEWTO"))

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

		# tester l'unicité d'un username
		funcs.user_create(cursor, "NomUtilisateur", "1__Mdp__!")
		cursor.execute('SELECT username FROM `Users` WHERE username="NomUtilisateur"')
		self.assertEqual(len(cursor.fetchall()), 1)

	def test_user_get_keys(self):
		keys = funcs.user_get_keys(cursor, "DestroyerDu75")
		self.assertTrue(isinstance(keys, tuple))
		self.assertEqual(len(keys), 4)
		for key in keys:
			self.assertTrue(isinstance(key, str))
			self.assertEqual(len(key), 128)

	def test_is_database_corrupted(self):
		self.assertFalse(funcs.is_database_corrupted(cursor))

		# idéalement il faudrait tester la non validité des champs un par un; la flemme
		cursor.execute("INSERT INTO `Users` VALUES(?, ?, ?, ?, ?, ?)", ["User_incorrect", "MdpNonValide", "1", "2", "3", "4"])
		self.assertTrue(funcs.is_database_corrupted(cursor))

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
