#!/usr/bin/python

"""
Plot sensor data & events using matplotlib. 
"""

import gramme
import matplotlib.pyplot as plt
from accelrationvector import AccelrationVector
from timekeeper import TimeKeeper

from logbook import Logger

log = Logger('apps: plotter', level=50)

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

if __name__ == '__main__':
	p = Plot(max_points=200, scaling=5)	
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