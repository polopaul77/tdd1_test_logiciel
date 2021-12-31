import numpy as np
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
		self.assertEqual(funcs.is_geo([5]), True)
		self.assertEqual(funcs.is_geo([0,0,0,0]), True)
		self.assertEqual(funcs.is_geo([4,-4,4,-4]), True)
		self.assertEqual(funcs.is_geo([1,2,3,4]), False)
		self.assertEqual(funcs.is_geo([-6,-9,7,1,-1,0]), False)
		self.assertEqual(funcs.is_geo([2,6,18,4]), False)


if __name__ == '__main__':
	unittest.main()
