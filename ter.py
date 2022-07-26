# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 17:19:51 2018

@author: Hewitt
"""

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from pylab import rcParams
rcParams['figure.figsize'] = 10, 7

#known Information
LFL = 0.075  # methane in air
UFL = 0.36 # methane in air
z = 3/2 # oxygen stoichiometric coefficient
LOC = 0.10

def __ter__():
	x = np.linspace(0,1)
	xair,yair = point(0.79*(1-x),x)
	plt.plot(xair,yair,'b',label='Air Line')

def point(x1,x2):
	x3 = 1-x1-x2
	x = 1-0.5*x2-x3
	y = (3**.5)/2*x2
	return(x,y)

def grid(spacing = 0.2):
	y = (3**.5)/2
	plt.plot([0,1],[0,0],'k')
	plt.plot([0,0.5],[0,y],'k')
	plt.plot([0.5,1],[y,0],'k')
	x_air1,y_air1 = point(0,1)
	x_air2,y_air2 = point(0.79,0)
	plt.plot([x_air1,x_air2],[y_air1,y_air2],'-b',label='Air')
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
	plt.text(0.45,-0.05,'Nitrogen',color='g')
	plt.text(0,-0.05,"0",color='g')
	plt.text(1,-0.05,"1",color='g')
	plt.text(0.15,0.50,'Oxygen',color='b',rotation=50)
	plt.text(-0.025,0.025,"1",color='b')
	plt.text(0.455,0.975*3**.5/2,"0",color='b')
	plt.text(0.75,0.45,'Fuel',color='r',rotation=-50 )
	plt.text(0.54,0.975*3**.5/2,'1',color='r')
	plt.text(1.01,0.025,"0",color='r')
	
def LFL_(lfl):
	xs = [1-0.5*lfl,0.5*lfl]
	ys = [(3**.5)/2*lfl,(3**.5)/2*lfl]
	return(xs,ys)

def UFL_line(lfl,ufl,stoich):
	xlfl,ylfl = point(0.79-lfl,lfl) # intercetp of stoich and LFL lines
	xufl,yufl = point((1-ufl)*0.79,ufl) # x and y of UFL
	xstoich = 3**.5/2*stoich
	ystoich = 3**.5/2*stoich
	mstoich = ystoich/(xstoich-1)
	#print(xlfl,ylfl,xufl,yufl,xstoich,ystoich,mstoich)
	x_sl  = (ylfl-ystoich)/mstoich+xstoich
	#x0 = 	
	mufl = (ylfl-yufl)/(x_sl-xufl)
	#print(x_sl,mufl,theta,dx,x)
	plt.plot([x,x_sl+dx],[y,0])

def LOC_line(LOC):
	x1,y1 = point(0,1-LOC)
	x2,y2 = point(1-LOC,0)
	plt.plot([x1,x2],[y1,y2],'-.b',label='LOC')
	
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
	
def stoich(z):
	xstoich,ystoich = point(0,1-z/(z+1))
	plt.plot([xstoich,1],[ystoich,0],'g',label='Stoichiometric Line')
	


xLFL,yLFL = LFL_(LFL)
xlfl,ylfl = point((1-LFL)*0.79,LFL)
xufl,yufl = point((1-UFL)*0.79,UFL)


#flammability limit data
LOC_line(LOC)
flammability_fill(UFL,LFL,z,LOC)
stoich(z)
plt.scatter(xlfl,ylfl,c='r',label='LFL,UFL')
plt.scatter(xufl,yufl,c='r')
plt.plot(xLFL,yLFL,'r',label="LFL")

grid(spacing=0.1)
plt.xlim(-0.1,1.1)
plt.ylim(-0.1,0.9)
plt.xticks([])
plt.yticks([])
plt.legend()
plt.show()

		