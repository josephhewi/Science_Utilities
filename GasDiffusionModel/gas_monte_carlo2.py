import numpy as np
from numpy import cos,sin
from numpy.random import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(0,0,0,s=60,c='k')	
ax.set_xlim3d(-1e4,1e4)
ax.set_ylim3d(-1e4,1e4)
ax.set_zlim3d(-1e4,1e4)
plt.draw()
plt.pause(5)
hist = 100
histories = np.zeros((hist,3))
paths = 5
mass = 40
velocity = np.sqrt(2200**2/mass)
cycles = 100

for i in range(0,cycles):
	plt.clf()
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(0,0,0,s=60,c='k')
	ax.set_xlim3d(-1e4,1e4)
	ax.set_ylim3d(-1e4,1e4)
	ax.set_zlim3d(-1e4,1e4)
	for x in range(0,hist):
		for j in range(0,5):
			phi = random()*180
			theta = random()*360
			d = np.array([ cos(theta)*cos(abs(phi-90)), sin(theta)*cos(abs(phi-90)), (sin(phi-90))])*velocity
			histories[x] = histories[x] + d
		ax.scatter(histories[x,0],histories[x,1],histories[x,2])
	plt.draw()
	plt.pause(1e-6)

	plt.draw()
	plt.pause(5)
	#plt.savefig("{}-{}.png".format(i,angle))

raw_input()




	
		
		