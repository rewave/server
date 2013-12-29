from basefilter import BaseFilter

class DecimalFilter(BaseFilter):
	"""Strip data upto n decimal points"""
	def __init__(self, ax, ay, precision=2):
		super(DecimalFilter, self).__init__(ax, ay)
		self.precision = precision
	
	def _apply(self, p):
		p = round(p, self.precision)
		return p if p**2> 0.001 else 0