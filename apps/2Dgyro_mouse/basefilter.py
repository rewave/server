class BaseFilter(object):
	"""filtering of x,y accelration"""
	def __init__(self, ax, ay):
		super(BaseFilter, self).__init__()
		self.ax = ax
		self.ay = ay

	def _apply(self,p):
		'''
		Override and apply the algorithm in individual data points
		(Make the Filter upgradable)
		'''
		pass

	def update(self, ax, ay):
		self.ax = ax
		self.ay = ay
		return self

	def filtered(self):
		return (self._apply(self.ax), self._apply(self.ay))