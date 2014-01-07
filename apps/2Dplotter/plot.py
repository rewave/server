#!/usr/bin/python

import matplotlib.pyplot as plt
from accelrationvector import AccelrationVector
from timekeeper import TimeKeeper

class Plot(object):
	"""Hold the real plots"""
	def __init__(self, figsize=(16,12), max_points=20, scaling=4, y_min=-2, y_max=2):
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
			axis.set_ylim([y_min, y_max])
			axis.set_xlim([1.0/self.T.scaling, self.T.max_points/self.T.scaling])

		plt.ion()
		plt.tight_layout()
		plt.show()

	def update_axes(self):
		for direction, axis in self.axes.iteritems():
			change = self.T.max_points/self.T.scaling - 1.0/self.T.scaling
			xmin,xmax = axis.get_xlim()

			axis.set_xlim(xmin+change, xmax+change)
				
	def update(self, ax, ay, az):
		self.A.update([ax, ay, az]) 
		self.T.tick()
		i = 0  
		for direction, axis in self.axes.iteritems():
			if self.T.points[-1] >= self.max_points/self.scaling :
				axis.set_axis_bgcolor('white')
			axis.plot(self.T.points , self.A[direction], alpha=0.5, linewidth=0.05, color='red')
		plt.draw()