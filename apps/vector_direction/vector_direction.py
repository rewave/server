#!/usr/bin/python

"""
Determin vector direction left or right
"""

import gramme, struct, time
from pykeyboard import PyKeyboard

from logbook import Logger

k = PyKeyboard()
movement = 0
log = Logger('apps: vector_direction', level=50)

if __name__ == '__main__':
	@gramme.server(3030)
	def plotter(data):
		global k, movement
		try:
			data = struct.unpack('ffffff', data[4:28])#ax,ay,az,wx,wy,wz
			length = (float(data[0])**2 + float(data[1])**2)**0.5
			if length >= 2.5 and movement == 0:
				log.info("Length of vector : %s"%length)
				movement = 1
				if float(data[0])>0:
					log.info("Accelration towards right")
					k.tap_key(k.right_key)
				else:
					log.info("Accelration towards left")
					k.tap_key(k.left_key)	
			else:
				movement = 0
		except KeyboardInterrupt:
			raise #let gramme handle this