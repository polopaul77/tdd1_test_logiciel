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

	def test_avg_int(self):
		self.assertEqual(funcs.avg_int([1,2,3,4,5]),3)
		self.assertEqual(funcs.avg_int([-2,-4]),-3)
		self.assertEqual(funcs.avg_int([-2,-1,1,2]),0)
		self.assertEqual(funcs.avg_int([0,0,0,0,0]),0)
		self.assertEqual(funcs.avg_int([13]),13)

if __name__ == '__main__':
	unittest.main()
