#!/usr/bin/python

"""
Plot sensor data & events using matplotlib. 
"""

import gramme, struct
from plot import Plot

from logbook import Logger

log = Logger('apps: plotter', level=50)

if __name__ == '__main__':
	p = Plot(max_points=200, scaling=1, y_min=-4, y_max=4)	
	data_points = 0
	@gramme.server(3030)
	def plotter(data):
		global p, data_points
		try:
			data = struct.unpack('ffffff', data[4:28])#data.split(',')[2:4] #x,y accelration
			data_points += 1
			if data_points > p.max_points : 
				p.update_axes()
				data_points = 0
			log.info("Data received : %s"%str(data))
			p.update(float(data[0]), float(data[1]), float(data[2]))
		except KeyboardInterrupt:
			raise #let gramme handle this