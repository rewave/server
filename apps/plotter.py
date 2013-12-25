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
			log.error('Direction %s is not defined'%direction)
			return []

	def _fix_length(self, direction):
		try:
			self.a[direction] = self.a[direction][-self.max_modulus:]
		except KeyError as e:
			log.error('Direction %s is not defined'%direction)
			return []	
	
	def append(self, direction, value):
		try:
			self.a[direction].append(value)
			self._fix_length(direction)
			return self.a[direction]
		except KeyError as e:
			log.error('Direction %s is not defined'%direction)
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


class Plot(object):
	"""Hold the real plots"""
	def __init__(self, figsize=(16,12)):
		super(Plot, self).__init__()
		self.figsize = figsize
		self.figure = plt.figure(figsize=self.figsize)
		self.axes = {
			'x':self.figure.add_subplot(311),
			'y':self.figure.add_subplot(312),
			'z':self.figure.add_subplot(313)
		}

		#draw the first version
		for acc, axis in self.axes.iteritems():
			axis.axhline(0)
			axis.set_title(acc)
			axis.set_ylim([-2,2])
			axis.set_xlim(1,100)

		plt.ion()
		plt.tight_layout()
		plt.show()

	def update(self, A, t):
		#A, t are AccelrationVector and TimeKeeper objects
		for direction, axis in self.axes.iteritems():
			axis.scatter(t.get(), A[direction])

	

		

A = AccelrationVector(max_modulus=5)
t = TimeKeeper(max_points=5)
p = Plot()

@gramme.server(3030)
def plotter(data):
	global A, t, p
	(x,y,z) = data.split(',')[2:]
	p.update()
	try:
		plt.draw()
	except KeyboardInterrupt:
		raise #let gramme handle this