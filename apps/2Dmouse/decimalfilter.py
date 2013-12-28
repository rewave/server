from basefilter import BaseFilter

class DecimalFilter(BaseFilter):
	"""Strip data upto n decimal points"""
	def __init__(self, ax, ay, precision=2):
		super(DecimalFilter, self).__init__(ax, ay)
		self.precision = precision
	
	def _apply(self, p):
		return round(p, self.precision)