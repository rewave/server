#!/usr/bin/python

"""
Determine vector direction left or right
"""

import gramme, datetime, time
from os import rename
from logbook import Logger
import library.data_formatter.iPhone as iPhone

base_time = time.time()
log = Logger('log_data.py', level=0)

name = raw_input("Name the log (blank for current time stamp) : ")

if name : name += ".txt"
else : name = str(datetime.datetime.now())+".txt"

log_file = open("analysis/logs/"+name, "w+")


@gramme.server(3030)
def main(data):
	try:
		data = iPhone.convert(data)
		line = str(time.time()-base_time)
		for observation in data:
			line += ",%s"%str(observation)
		log.info(line)
		log_file.write(line+"\n")
	except KeyboardInterrupt:
		log_file.close()
		raise #let gramme handle this