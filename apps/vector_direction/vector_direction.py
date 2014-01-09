#!/usr/bin/python

"""
Determine vector direction left or right
"""

import gramme, struct, time
from pykeyboard import PyKeyboard

from logbook import Logger

k = PyKeyboard()
movement = 0
motion_log = {'left':0, 'right':0}

log = Logger('apps: vector_direction', level=0)

if __name__ == '__main__':
	@gramme.server(3030)
	def plotter(data):
		global k, movement
		try:
			data = struct.unpack('ffffff', data[4:28])#ax,ay,az,wx,wy,wz
			length = (float(data[0])**2 + float(data[1])**2)**0.5
			if length >= 2.5:
				log.info("Data received is %s"%str(data))
				if float(data[0])>0:
					motion_log['right'] +=data[0]
				else:
					motion_log['left'] +=data[1]
			else:
				if motion_log['left'] > motion_log['right']:
					log.info("Accelration towards left")
					k.tap_key(k.right_key)	
				if motion_log['left'] < motion_log['right']:
					log.info("Accelration towards right")
					#k.tap_key(k.right_key)	
					
				motion_log['left'] = motion_log['right'] = 0

		except KeyboardInterrupt:
			raise #let gramme handle this