#! /usr/bin/python

import struct

def convert(data):
	#data is raw packet received by server while using Sensor Streamer by FNI app on iphone
	return struct.unpack('ffffff', data[4:28])#ax,ay,az,wx,wy,wz
