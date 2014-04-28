#!/usr/bin/python
from database import Pattern, MotionLog

class PatternHolder(object):
	def __init__(self, template_name=None, stream=False, max_size = 40, key_code=None):
		self.template_name 	= template_name
		self.pattern_matrix = []
		self.key_code 		= key_code
		self.stream 		= stream
		self.max_size 		= max_size
		self._retrieve_pattern_matrix(template_name)

	def _retrieve_pattern_matrix(self, template_name):
		if not self.stream:
			logs = MotionLog.select().join(Pattern, on=MotionLog.pattern).where(Pattern.name==template_name)
			for l in logs:
				self.pattern_matrix.append([l.timestamp, l.ax, l.ay, l.az, l.gx, l.gy, l.gz])
		else:
			t = self.max_size
			while(t>0):
				t = t-1
				self.pattern_matrix.append([0,0,0,0,0,0,0])

	def get(self):
		return self.pattern_matrix

	def put(self, acceleration_instance):
		#delete 0th term and append the latest
                if len(self.pattern_matrix) >0:
                        del(self.pattern_matrix[0])
                try:
                        self.pattern_matrix.append([float(i) for i in acceleration_instance])
                except ValueError, e:
                        pass

	def truncate(self):
                self.pattern_matrix = []


def main():
	left_wave = PatternHolder(template_name="right_wave")
	print left_wave.get()

	stream = PatternHolder(stream=True)
	print stream.get()

	
if __name__ == '__main__':
	main()