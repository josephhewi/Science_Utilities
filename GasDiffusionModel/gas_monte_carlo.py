import numpy as np
from numpy import cos,sin
from numpy.random import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(0,0,0,s=60,c='k')
histories = 10000
paths = 10



mass = 40
velocity = np.sqrt(2200**2/mass)
#mean_distance = 
mean_posn = np.array([0,0,0])
particle_history = np.arange(0)
for particle in range(0,histories):
	position = np.array([0,0,0])
	for step in range(0,paths):
		phi = random()*180
		theta = random()*360
		d = np.array([ cos(theta)*cos(abs(phi-90)), sin(theta)*cos(abs(phi-90)), (sin(phi-90))])*velocity
		position = position + d
	ax.scatter(position[0],position[1],position[2])
	mean_posn = mean_posn+(position/(particle+1))
	particle_history = np.append(particle_history, np.sqrt(position[0]**2+position[1]**2+position[2]**2))
	ax.view_init(30, particle)
	#plt.title('mean position {0},{1},{2}'.format(mean_posn[0],mean_posn[1],mean_posn[2]))
	plt.draw()
	plt.savefig("{0}.png".format(particle))
print(particle_history)
	
		
		