#!/usr/bin/python

"""
Plot sensor data & events using matplotlib. 
"""

import gramme
import matplotlib.pyplot as plt

from logbook import Logger

log = Logger('apps: plotter', level=50)

class AccelrationVector(object):
	"""Data strucuture to hold and manipulate accelration vector"""
	
	def __init__(self, max_modulus=20):
		#max_modulus : max data points the array should hold for each direction
		super(AccelrationVector, self).__init__()
		self.a = {'x':[], 'y':[], 'z':[]}
		self.max_modulus = max_modulus

	def __getitem__(self, direction):
		try:
			return self.a[direction]
		except KeyError as e:
			log.error("Direction %s is not defined"%direction)
			return []

	def _fix_length(self, direction):
		try:
			self.a[direction] = self.a[direction][-self.max_modulus:]
		except KeyError as e:
			log.error("Direction %s is not defined"%direction)
			return []	
	
	def append(self, direction, value):
		try:
			self.a[direction].append(value)
			self._fix_length(direction)
			return self.a[direction]
		except KeyError as e:
			log.error("Direction %s is not defined"%direction)
			return []

class TimeKeeper(object):
	"""Data structure to store and manipulate time. Time is added in steps"""
	
	def __init__(self, max_points=20):
		super(TimeKeeper, self).__init__()
		self.t = []
		self.max_points = max_points

	def _fix_length(self):
		self.t = self.t[-self.max_points:]

	def tick(self, time):
		self.t.append(time)	
		self._fix_length()
		return self.t

	def get(self):
		return self.t

	def get_t_range(self):
		try:
			return (self.t[0]-0.06, self.t[-1]+0.09)
		except IndexError as e:
			return (-1,1)


A = AccelrationVector(max_modulus=5)
t = TimeKeeper(max_points=5)

figure = plt.figure(figsize=(16,4))
axes = {
	"Ax":figure.add_subplot(131),
	"Ay":figure.add_subplot(132),
	"Az":figure.add_subplot(133)
}

for acc, axis in axes.iteritems():
	axis.grid(True)
	axis.axhline(0)
	axis.set_title(acc)
	axis.set_ylim([-2,2])
	axis.set_xlim(t.get_t_range())
plt.ion()
plt.show()

@gramme.server(3030)
def plotter(data):
	global A, t
	data = data.split(',')[1:]

	t.tick(float(data[0]))
	A.append('x', float(data[1]) )
	A.append('y', float(data[2]) )
	A.append('z' ,float(data[3]) )

	axes["Ax"].plot(t.get(), A['x'], color="red", linewidth=1.0, linestyle="-")
	axes["Ay"].plot(t.get(), A['y'], color="green", linewidth=1.0, linestyle="-")
	axes["Az"].plot(t.get(), A['z'], color="blue", linewidth=1.0, linestyle="-")

	for acc, axis in axes.iteritems():
		axis.set_xlim(t.get_t_range())
	try:
		plt.draw()
	except KeyboardInterrupt:
		raise #let gramme handle this