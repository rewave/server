from logbook import Logger

log = Logger('apps: plotter', level=50)

class AccelrationVector(object):
	"""Data strucuture to hold and manipulate accelration vector"""
	
	def __init__(self, max_points=100):
		#max_points : max data points the array should hold for each direction
		super(AccelrationVector, self).__init__()
		self.a = {'x':[], 'y':[], 'z':[]}
		self.max_points = max_points

	def __getitem__(self, direction):
		try:
			return self.a[direction]
		except KeyError as e:
			log.error('Direction %s is not defined'%direction)
			return []

	def _fix_length(self, direction):
		try:
			if len(self.a[direction]) > self.max_points :
				self.a[direction] = self.a[direction][-self.max_points:]  
		except KeyError as e:
			log.error('Direction %s is not defined'%direction)
	
	def _add_single(self, direction, value):
		try:
			self.a[direction].append(value)
			self._fix_length(direction)
			log.info("Accelration in direction %s : %s"%(direction, str(self.a[direction])))
			return self.a[direction]
		except KeyError as e:
			log.error('Direction %s is not defined'%direction)
			return []

	def update(self, a_point):
		directions = ['x','y','z']
		try:
			for i in range(3):
				self._add_single(directions[i], a_point[i])
		except KeyError as e:
			log.error('Direction %s is not defined'%direction)

	def truncate(self):
		self.a = {'x':[], 'y':[], 'z':[]}