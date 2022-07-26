# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 22:43:13 2018

@author: Hewitt
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


def RK45(f,t,h,y0):
	k1 = h*f(t,          y0)
	k2 = h*f(t+h*(1/4),  y0+k1*(1/4))
	k3 = h*f(t+h*(3/8),  y0+k1*(3/32)+     k2*(9/32))
	k4 = h*f(t+h*(12/13),y0+k1*(1932/2197)-k2*(7200/2197)+ k3*(7296/2197))
	k5 = h*f(t+h,        y0+k1*(439/216)-  k2*(8)+         k3*(3680/513)+  k4*(-845/4104))
	k6 = h*f(t+h*(1/2),  y0-k1*(8/27)+     k2*(2)-         k3*(3544/2565) +k4*(1859/4104)-k5*(11/40))
		
	z1 = y0 + k1*(16/135) + k3*(6656/12825) + k4*(28561/56430)- k5*(9/50) + k6*(2/55)
	y1 = y0 + k1*(25/216) + k3*(1408/2565) +  k4*(2197/4104)-   k5*(1/5)
	return(y1,z1)

def RKF45(f,t0,tf,y0,tolerance=1e-6,hmin=1e-3,hmax=1e-3,maximum_iterations=1000):
	h = (tf-t0)/(maximum_iterations/2)
	t  = t0
	counter = 0
	T_error =0
	ts = np.arange(0)
	ys = y0
	while (t < tf and counter<maximum_iterations):
		counter+=1
		y1,z1 = RK45(f,t,h,y0)
		error = abs(np.max((z1-y1)/z1))
		if (error>tolerance  or error<tolerance/10):
			h = h*(error/tolerance)**0.2
			if (h<hmin):
				h = hmin
			elif (h>hmax):
				h = hmax
			y1,z1 = RK45(f,t,h,y0)
		ys = np.append(ys,y0)
		ts = np.append(ts,t)
		print y1
		print y0
		y0 = y1
		t+=h
		#print(t,y0)
		ys = np.vstack((ys,y0))
		print ys
		ts = np.append(ts,t)
	return ts, ys

def f(y,x):
	return(np.array([0,1]))
	
print(RKF45(f,0,1,([0,0])))
		