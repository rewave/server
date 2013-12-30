#!/usr/bin/python

"""
Plot sensor data & events using matplotlib. 
"""

import gramme
from accelrationvector import AccelrationVector
from timekeeper import TimeKeeper
from plot import Plot

from logbook import Logger

log = Logger('apps: plotter', level=50)

if __name__ == '__main__':
	p = Plot(max_points=80, scaling=2, y_min=-4, y_max=4)	
	data_points = 0
	@gramme.server(3030, poll_interval=1/73)
	def plotter(data):
		global p, data_points
		try:
			data = data[:-1].split(',')[2:]
			data_points += 1
			if data_points > p.max_points : 
				p.update_axes()
				data_points = 0
			log.info("Data received : %s"%str(data))
			p.update(float(data[0]), float(data[1]), float(data[2]))
		except KeyboardInterrupt:
			raise #let gramme handle this