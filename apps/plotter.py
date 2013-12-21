#!/usr/bin/python

"""
Plot sensor data & events using matplotlib. 
"""

import gramme
import matplotlib.pyplot as plt

Ax, Ay, Az, t_list = [],[],[],[]
t = 0
t_step = 0.03


figure = plt.figure(figsize=(12,7.41))
axes = {
	"Ax":figure.add_subplot(231),
	"Ay":figure.add_subplot(232),
	"Az":figure.add_subplot(233)
}

for acc, axis in axes.iteritems():
	axis.grid(True)
	axis.axhline(0)
	axis.set_title(acc)
	axis.set_ylim([-2,2])
plt.ion()
plt.show()

@gramme.server(3030)
def plotter(data):
	global t, t_step
	data = data.split(',')[2:]
	Ax.append(float(data[0]))
	Ay.append(float(data[1]))
	Az.append(float(data[2]))
	t_list.append(t)
	t+=t_step

	axes["Ax"].plot(t_list, Ax, color="red", linewidth=1.0, linestyle="-")
	axes["Ay"].plot(t_list, Ay, color="green", linewidth=1.0, linestyle="-")
	axes["Az"].plot(t_list, Az, color="blue", linewidth=1.0, linestyle="-")


	try:
		plt.draw()
	except KeyboardInterrupt:
		print t_list
		raise #let gramme handle this