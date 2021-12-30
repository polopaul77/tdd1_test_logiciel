import funcs
import unittest

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

if __name__ == '__main__':
	unittest.main()
