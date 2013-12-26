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


class Plot(object):
	"""Hold the real plots"""
	def __init__(self, figsize=(16,12), max_points=20, scaling=4):
		super(Plot, self).__init__()
		self.figsize = figsize
		self.figure = plt.figure(figsize=self.figsize, facecolor='#ffffff')
		self.axes = {
			'x':self.figure.add_subplot(311),
			'y':self.figure.add_subplot(312),
			'z':self.figure.add_subplot(313)
		}
		self.max_points = max_points
		self.scaling = scaling
		self.A = AccelrationVector(max_points=self.max_points)
		self.T = TimeKeeper(max_points=self.max_points, scaling=self.scaling)

		if self.A.max_points != self.T.max_points :
			raise ValueError("TimeKeeper and AccelrationVector objects should have same max ")

		#draw the first version
		for acc, axis in self.axes.iteritems():
			axis.set_title(acc)
			axis.set_ylim([-2,2])
			axis.set_xlim([1.0/self.T.scaling, self.T.max_points/self.T.scaling])
			#axis.axis("off")

		plt.ion()
		plt.tight_layout()
		plt.show()

	def update_axes(self):
		for direction, axis in self.axes.iteritems():
			axis.set_xlim([self.T.points[-1], self.T.points[-1]+self.T.scaling*self.T.max_points])
				
	def update(self, ax, ay, az):
		self.A.update([ax, ay, az]) 
		self.T.tick()
		i = 0  
		for direction, axis in self.axes.iteritems():
			if self.T.points[-1] >= self.max_points/self.scaling :
				axis.set_axis_bgcolor('white')
			axis.plot(self.T.points , self.A[direction], alpha=0.5, linewidth=0.15)
		plt.draw()

p = Plot(max_points=40, scaling=1)
data_points = 0
@gramme.server(3030)
def plotter(data):
	global p, data_points
	try:
		data = data[:-1].split(',')[2:]
		data_points += 1
		if data_points > p.max_points*p.scaling : 
			p.update_axes()
			data_points = 0
		log.info("Data received : %s"%str(data))
		p.update(float(data[0]), float(data[1]), float(data[2]))
	except KeyboardInterrupt:
		raise #let gramme handle this