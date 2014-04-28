#!/usr/bin/python

from database import Pattern, MotionLog
from pykeyboard import PyKeyboard
import csv

k = PyKeyboard()

class CsvPattern(object):
	def __init__(self, template_name=None, key_code=None):
		self.template_name 	= template_name
		self.pattern_matrix = []
		self.key_code 		= key_code
		with open("templates/"+template_name+".txt", "rb") as csv_file:
			reader = csv.reader(csv_file)
			for row in reader:
				self.pattern_matrix.append(row)
	
	def get(self):
		return self.pattern_matrix

def main():
	p = Pattern()
	m = MotionLog()

	patterns_to_load = [
		CsvPattern(template_name="left_wave", key_code=k.left_key),
		CsvPattern(template_name="right_wave", key_code=k.right_key), 
		CsvPattern(template_name="flick_up", key_code=k.up_key),
		CsvPattern(template_name="flick_down", key_code=k.down_key)
	]

	for csv_pattern in patterns_to_load:
		current = p.create(name=csv_pattern.template_name, key_code=csv_pattern.key_code)
		print "creating " + csv_pattern.template_name
		for row in csv_pattern.get(): #we have the matrix here
			print "\t creating motion log point"
			m.create(pattern=current, timestamp=row[0], ax=row[1], ay=row[2], az=row[3], gx=row[4], gy=row[5], gz=row[6])

if __name__ == '__main__':
	main()