#!/usr/bin/python

"""
Determine vector direction left or right
"""

import gramme, struct, time
from pykeyboard import PyKeyboard

from logbook import Logger

k = PyKeyboard()
motion_log = []

log = Logger('apps > vector_direction', level=0)

if __name__ == '__main__':
	@gramme.server(3030)
	def plotter(data):
		global k, motion_log
		try:
			data = struct.unpack('ffffff', data[4:28])#ax,ay,az,wx,wy,wz
			length = (float(data[0])**2 + float(data[1])**2)**0.5
			if length >= 1.5:
				#log.info("Data received is %s"%str(data))
				motion_log.append([data[0], data[1]])
			else:
				try:
					if motion_log[0][0] > 0 and motion_log[-1][0] < 0:#maybe left
						log.info("Left wave encountered")
						k.tap_key(k.right_key)
					if motion_log[0][0] < 0 and motion_log[-1][0] > 0:
						log.info("Right wave encountered")
						k.tap_key(k.left_key)
					motion_log = [] #flush
				except IndexError as e:
					#no elements added to motion log
					pass 

		except KeyboardInterrupt:
			raise #let gramme handle this