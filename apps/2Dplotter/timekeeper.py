from logbook import Logger

log = Logger('apps: plotter', level=50)

class TimeKeeper(object):
	"""Data structure to store and manipulate time. Time is added in steps"""
	
	def __init__(self, max_points=100, scaling=2):
		#scaling should be a factor of max points for divisions to be discrete
		super(TimeKeeper, self).__init__()
		self.points = []
		self.max_points = max_points
		self.scaling = scaling

	def _fix_length(self):
		if len(self.points) > self.max_points : 
			self.points = self.points[-self.max_points:]

	def tick(self):
		try:
			self.points.append(self.points[-1]+1.0/self.scaling)
		except IndexError as e:
			self.points.append(1.0/self.scaling)
		self._fix_length()
		log.info("Time points : %s"%str(self.points))

	def truncate(self):
		self.points = []