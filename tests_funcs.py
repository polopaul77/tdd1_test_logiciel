import funcs
import unittest

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

if __name__ == '__main__':
	unittest.main()
