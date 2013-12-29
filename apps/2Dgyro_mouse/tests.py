#!/usr/bin/python

from basefilter import BaseFilter
from decimalfilter import DecimalFilter
import unittest

class TestBaseFilter(unittest.TestCase):
	def setUp(self):
		self.bf = BaseFilter(1,1)

	def tearDown(self):
		self.bf = None
		
	def test_filter_return_none(self):
		#method has not been overridden yet
		self.assertEqual(self.bf.filtered(), (None, None))


class TestDecimalFilter(unittest.TestCase):
	def setUp(self):
		self.df1 = DecimalFilter(1.2421,1.4324, precision=2)
		self.df2 = DecimalFilter(1.2421,1.4324, precision=3)

	def tearDown(self):
		self.df1 = self.df2 = None

	def test_filter_precision(self):
		self.assertEqual(self.df1.filtered(), (1.24, 1.43))
		self.assertEqual(self.df2.filtered(), (1.242, 1.432))

	def test_update(self):		
		self.assertEqual(self.df1.update(2.2421,2.4324).filtered(), (2.24, 2.43))
		self.assertEqual(self.df2.update(2.2421,2.4324).filtered(), (2.242, 2.432))

if __name__ == '__main__':
	unittest.main()