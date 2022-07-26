# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 08:31:57 2018

@author: Joe Hewitt
"""

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from pylab import rcParams
rcParams['figure.figsize'] = 10, 8.66

UFL = 0.08
LFL = 0.01
z = 25/2
LOC = z*LFL

# Point: x1 is species 1 mole fraction and x2 is species 2 mole fraction
def point(x1,x2): 
	x3 = 1-x1-x2
	x = 1-0.5*x2-x3
	y = (3**.5)/2*x2
	return(x,y)

def grid(ax,spacing = 0.2,
		 name1='Species 1',name2='Species 2',name3='Species 3'):
	y = (3**.5)/2
	ax.plot([0,1],[0,0],'k')
	ax.plot([0,0.5],[0,y],'k')
	ax.plot([0.5,1],[y,0],'k')
	x2s = np.arange(0,1,spacing)
	for x in x2s:
		xs = [1-0.5*x,0.5*x]
		ys = [(3**.5)/2*x,(3**.5)/2*x]
		ax.plot(xs,ys,':r',alpha=0.5)
		xs = [x,0.5*(1+x)]
		ys = [0,3**.5/2*(1-x)]
		ax.plot(xs,ys,':g',alpha=0.5)
		xs = [0.5*(1-x),1-x]
		ys = [3**.5/2*(1-x),0]
		ax.plot(xs,ys,':b',alpha=0.5)
	# -------------------------------------------------------------
	ax.text(0.5,-0.03,name1,color='g',
		 horizontalalignment='center',verticalalignment='center',)
	ax.text(0,-0.03,"0",color='g')
	ax.text(1,-0.03,"1",color='g')
	# -------------------------------------------------------------
	ax.text(0.77,0.43,name2,color='r',rotation=-60,
		 horizontalalignment='center',verticalalignment='center',)
	ax.text(0.52,0.86,'1',color='r')
	ax.text(1.025,0,"0",color='r')
	# -------------------------------------------------------------
	ax.text(0.22,0.43,name3,color='b',rotation=60,
		 horizontalalignment='center',verticalalignment='center',)
	ax.text(-0.025,0,"1",color='b')
	ax.text(0.46,0.86,"0",color='b')
	
def flammability_autofill(UFL,LFL,z,LOC,ax):
	xair1,yair1 = point(0,1) #air line
	xlfl,ylfl = point((1-LFL)*0.79,LFL) #lower flamability limit line
	xufl,yufl = point((1-UFL)*0.79,UFL) #upper flamability limit line
	xstoich,ystoich = point(0,1-z/(z+1)) # stoichiometric line
	xloc1,yloc1 = point(0,1-LOC) #lower oxygen limit line
	xloc2,yloc2 = point(1-LOC,0)
	#slopes
	msto = (0-ystoich)/(1-xstoich)
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
	#plot all calculated information
	ax.plot([xair1,0.79],[yair1,0],c='b',label='Air')
	ax.scatter([xlfl,xufl],[ylfl,yufl],c='r',label='LFL and UFL')
	ax.plot([1-0.5*LFL,0.5*LFL],[(3**.5)/2*LFL,(3**.5)/2*LFL],
		 c='r',label='LFL')
	ax.plot([xloc1,xloc2],[yloc1,yloc2],c='orange',label='LOC')
	ax.plot([xstoich,1],[ystoich,0],'g',label='Stoichiometric Line')
	ax.fill_between(x,y1,y2,label='flammability region',color='r',alpha=0.2)
	
def inert_from_1(z,LFL,ax):
	OFSC = LFL/(1-z*LFL/0.21)
	xo,yo = point(0,1)
	xS,yS = point((1-OFSC),OFSC)
	ax.scatter([xo,xS,0.79],[yo,yS,0],color='k')
	ax.plot([xo,xS,0.79],[yo,yS,0],':m',linewidth=3,label='Inerting')
	ax.text(1,OFSC*.87,'S')
	ax.text(xo+0.01,yo+0.01,'Start',
		 horizontalalignment='center',verticalalignment='center',)
	ax.text(0.79,-0.03,'Stop',
		 horizontalalignment='center',verticalalignment='center',)
	print(OFSC)
	
fig,ax = plt.subplots()
grid(ax,spacing=0.05, 
	 name1=r'$N_2$ and $H_2O_{(g)}$',name2='Octane', name3='Oxygen')
flammability_autofill(UFL,LFL,z,LOC,ax)
inert_from_1(z,LFL,ax)
#interting 


plt.xlim(-0.1,1.1)
plt.ylim(-0.1,0.9)
plt.xticks([])
plt.yticks([])
plt.legend()
plt.show()

		