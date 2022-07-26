# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 08:31:57 2018

@author: Joe Hewitt
"""

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from pylab import rcParams
rcParams['figure.figsize'] = 10, 7

#known Information
misc_x1 = np.array([0.19,0.22,0.25,0.28,0.33,0.38,0.45,0.53,0.66,0.76,0.84,0.88,0.905,0.925,0.95,0.96,0.98,0.99])
misc_x2 = np.array([0.0,0.12,0.205,0.27,0.325,0.36,0.365,0.35,0.28,0.22,0.145,0.11,0.09, 0.065,0.045,0.03,0.01,0])		   
C = np.polyfit(misc_x1,misc_x2,4)




def point(x1,x2): # where x1 is species 1 mole fraction and x2 is species 2 mole fraction
	x3 = 1-x1-x2
	x = 1-0.5*x2-x3
	y = (3**.5)/2*x2
	return(x,y)

def grid(spacing = 0.2):
	y = (3**.5)/2
	plt.plot([0,1],[0,0],'k')
	plt.plot([0,0.5],[0,y],'k')
	plt.plot([0.5,1],[y,0],'k')
	x2s = np.arange(0,1,spacing)
	for x in x2s:
		xs = [1-0.5*x,0.5*x]
		ys = [(3**.5)/2*x,(3**.5)/2*x]
		plt.plot(xs,ys,':r',alpha=0.5)
		xs = [x,0.5*(1+x)]
		ys = [0,3**.5/2*(1-x)]
		plt.plot(xs,ys,':g',alpha=0.5)
		xs = [0.5*(1-x),1-x]
		ys = [3**.5/2*(1-x),0]
		plt.plot(xs,ys,':b',alpha=0.5)
	plt.text(0.45,-0.05,'Species 1',color='g')
	plt.text(0,-0.05,"0",color='g')
	plt.text(1,-0.05,"1",color='g')
	plt.text(0.15,0.50,'Species 3',color='b',rotation=50)
	plt.text(-0.025,0.025,"1",color='b')
	plt.text(0.455,0.975*3**.5/2,"0",color='b')
	plt.text(0.75,0.45,'Species 2',color='r',rotation=-50 )
	plt.text(0.54,0.975*3**.5/2,'1',color='r')
	plt.text(1.01,0.025,"0",color='r')

	
def flammability_fill(UFL,LFL,z,LOC):
	xsto1,ysto1 = point(0,1-z/(z+1))
	xsto2 = 1
	ysto2 = 0
	xloc1,yloc1 = point(0,1-LOC)
	xloc2,yloc2 = point(1-LOC,0)
	msto = (ysto2-ysto1)/(xsto2-xsto1)
	mloc = (yloc2-yloc1)/(xloc2-xloc1)
	#intercept of air and UFL
	X1,Y1 = point((1-UFL)*0.79,UFL)
	#intercept of air and LFL
	X2,Y2 = point((1-LFL)*0.79,LFL)
	#intercept of stoichiometric line and LFL
	X3 = (Y2-yloc1)/mloc+xloc1
	Y3 = mloc*(X3-xloc1)+yloc1
	#fill in Y value
	mupp = (Y3-Y1)/(X3-X1)
	Y4 = mupp*(X2-X1)+Y1
	x = [X1,X2,X3]
	y1 = [Y1,Y4,Y3]
	y2 = [Y1,Y2,Y3]
	plt.fill_between(x,y1,y2,label='flammability region',color='r',alpha=0.2)
	
def immiscible_bubble(x1,x2,ax):
	X,Y = point(x1,x2)
	ax.fill_between(X,Y,0,color='b',alpha=0.4,label='Immiscible Region')


#flammability limit data

immiscible_bubble(misc_x1,misc_x2,plt)


grid(spacing=0.05)
plt.xlim(-0.1,1.1)
plt.ylim(-0.1,0.9)
plt.xticks([])
plt.yticks([])
plt.legend()
plt.show()

		