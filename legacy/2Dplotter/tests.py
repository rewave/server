import unittest
from accelrationvector import AccelrationVector
from timekeeper import TimeKeeper

class TestAccelrationVector(unittest.TestCase):
	
	def setUp(self):
		self.max_points = 100
		self.A =  AccelrationVector(max_points=self.max_points)
		self.directions = ['x','y','z']

	def test_add_single_and___getitem__(self):
		self.A._add_single('x', 0)
		self.assertTrue(len(self.A['x']) == 1)
		self.assertTrue(len(self.A['y']) == 0)
		self.assertTrue(len(self.A['z']) == 0)

	def test_update(self):
		for i in range(10):
			self.A.update([i,i,i])
			self.assertTrue(len(self.A['x']) == i+1)
			self.assertTrue(len(self.A['y']) == i+1)
			self.assertTrue(len(self.A['z']) == i+1)

	def test_fix_length(self):
		for i in range(self.max_points+10):
			self.A.update([i,i,i])

		self.assertTrue(len(self.A['x']) == self.max_points)
		self.assertTrue(len(self.A['y']) == self.max_points)
		self.assertTrue(len(self.A['z']) == self.max_points)

	def test_truncate(self):
		for i in range(10):
			self.A.update([i,i,i])

		self.A.truncate()
		self.assertTrue(len(self.A['x']) == 0)
		self.assertTrue(len(self.A['y']) == 0)
		self.assertTrue(len(self.A['z']) == 0)

	def tearDown(self):
		self.A = None
		self.directions = None


class TestTimeKeeper(unittest.TestCase):
	def setUp(self):
		self.max_points = 100
		self.scaling = 4
		self.T = TimeKeeper(max_points=self.max_points, scaling=self.scaling)

	def test_tick(self):
		for i in range(self.max_points - 100):
			self.T.tick()
			self.assertTrue(len(self.T.points) == i+1)

	def test__fix_length(self):
		for i in range(self.max_points+10):
			self.T.tick()
		self.assertTrue(len(self.T.points) == self.max_points)

	def test_trucate(self):
		for i in range(self.max_points*self.scaling + 100):
			self.T.tick()
		self.T.truncate()
		self.assertTrue(len(self.T.points) == 0)


if __name__ == '__main__':
	unittest.main()