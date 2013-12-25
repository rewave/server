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
	
	def __init__(self, max_modulus=100):
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
			if len(self.a[direction]) > self.max_modulus : self.a[direction] = []  
		except KeyError as e:
			log.error('Direction %s is not defined'%direction)
	
	def _add_single(self, direction, value):
		try:
			self.a[direction].append(value)
			self._fix_length(direction)
			return self.a[direction]
		except KeyError as e:
			log.error('Direction %s is not defined'%direction)
			return []

	def update(self, A):
		#A = (x,y,z)
		directions = ['x','y','z']
		try:
			for direction in directions:
				self._add_single(direction, A[direction])
		except KeyError as e:
			log.error('Direction %s is not defined'%direction)


class TimeKeeper(object):
	"""Data structure to store and manipulate time. Time is added in steps"""
	
	def __init__(self, max_points=100):
		super(TimeKeeper, self).__init__()
		self.t = []
		self.max_points = max_points
		self.t0 = 0.0

	def _fix_length(self):
		if len(self.t) >= self.max_points : self.t = []

	def tick(self, time):
		self.t.append(time)
		self._fix_length()

	def get(self):
		return self.t

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

		plt.ion()
		plt.tight_layout()
		plt.show()
		self.t = 0

	def update(self, A, t):
		#A, t are AccelrationVector and TimeKeeper objects
		log.info("AccelrationVector in X direction is %s"%A['x'])
		log.info("Time list is : %s"%t.get())
		
		t_list = t.get()
		if self.t != t_list[0] : update_axis = True 
		else : update_axis = False

		for direction, axis in self.axes.iteritems():
			if update_axis : axis.set_xlim([t_list[0], t_list[0]+0.01])
			axis.plot(t_list, A[direction])
		plt.draw()

A = AccelrationVector(max_modulus=100)
t = TimeKeeper(max_points=100)
p = Plot()

@gramme.server(3030)
def plotter(data):
	global A, t, p
	try:
		data = data[:-1].split(',')[1:]
		log.info("Data received : %s"%str(data))
		time = float(data[0])
		acc_vector = {'x':float(data[1]), 'y':float(data[2]), 'z':float(data[3])}

		A.update(acc_vector)
		t.tick(time)
		p.update(A,t)
	except KeyboardInterrupt:
		raise #let gramme handle this