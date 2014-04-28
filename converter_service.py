#!/usr/bin/python

from database import Pattern, MotionLog
from pattern_holder import PatternHolder as CsvPattern
from pykeyboard import PyKeyboard

k = PyKeyboard()

def main():
	p = Pattern()
	m = MotionLog()

	patterns_to_load = [
		CsvPattern(template_name="left_wave", key_code=k.left_key),
		CsvPattern(template_name="right_wave", key_code=k.right_key), 
		CsvPattern(template_name="flick_up", key_code=k.up_key),
		CsvPattern(template_name="flick_down", key_code=k.down_key)
	]

	for pattern in patterns_to_load:
		current = p.create(name=pattern.template_name, key_code=pattern.key_code)
		for row in pattern.get(): #we have the matrix here
			m.create(pattern=current, timestamp=row[0], ax=row[1], ay=row[2], az=row[3], gx=row[4], gy=row[5], gz=row[6])

	
	

if __name__ == '__main__':
	main()