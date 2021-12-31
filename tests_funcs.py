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

if __name__ == '__main__':
	unittest.main()
