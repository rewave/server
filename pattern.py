#!/usr/bin/python
import csv

class Pattern(object):
	def __init__(self, template_name=None, stream=False, max_size = 40):
		self.template_name = template_name
		self.pattern_matrix = []

		if not stream:
			with open("templates/"+template_name, "rb") as csv_file:
				reader = csv.reader(csv_file)
				for row in reader:
					self.pattern_matrix.append(row)
		
		#pad both stream and template
		while len(self.pattern_matrix) < max_size:
			self.pattern_matrix.append([0, 0, 0, 0, 0, 0, 0]) #padding

	def get(self):
		return self.pattern_matrix

	def put(self, acceleration_instance):
		#delete 0th term and append the latest 
		del(self.pattern_matrix[0])
		self.pattern_matrix.append(acceleration_instance)

def main():
	letter_s = Pattern("letter_s.txt")
	print len(letter_s.get())

	stream = Pattern(stream=True)
	print stream.get()

if __name__ == '__main__':
	main()