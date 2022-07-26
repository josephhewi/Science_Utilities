# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:40:04 2018

@author: Joe Hewitt
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from numeric.RK45 import *

global Ac, D, thetas, MW, Fao, Po, To, G, cpa, R, Pao, Tr, Ua, alpha

#physical description of the system
Ac = 195.5 # cross sectional area (ft2)
D = (4*Ac/np.pi)**2 # diameter (ft)
R = 1.98 # gas constant
thetas = np.array([1,1,0,8]) # relative flows ([A,B,C,I])
phi = 0.45 # void fraction (unitless)
mu = 0.090 #
Dp = 0.0015
rho_b = 33.8
rho_o = 0.090

# energy balance starting point
Tao = 1264.67 # cooling fluid temeperature (R)
To = 1000 # initial temperature (R)
Tr = 1260 # reference temperature for dHr (R)
# heat capacity = sum( theta * (A+B*T+C*T^2)) 
A = np.array([7.208,5.371,8.511,6.248]) 
B = np.array([5.633e-3,2.323e-3,9.517e-3,8.778e-4])
C = np.array([-1.343e-6,-4.886e-7,-2.325e-6,-2.130e-8])
U = 10 # overall heat transfer coefficient (btu/h-ft2-R)
Ua = 4*U/(rho_b*D) # Ua/rhob

# material balance starting point
MW = np.array([64.066,31.998,80.066,28.0134]) # MW of ([A,B,C,I])
Fao = 0.188 # flow through an individual packed tube
Po = 1 # initial pressure (ATM)
G = Fao*np.sum(thetas*MW)
alpha = (G*Po*(1-phi))/(rho_b*Ac*rho_o*To)*((150*(1-phi)*mu)/(Dp)-1.75*G)
yao = 1/np.sum(thetas)
Pao = Po*yao # partial pressure = mole fraction in the ideal system
delta = -0.5
epsilon = yao*delta

# misc
Xo = 0

# initiailize input
y0 = np.array([Xo,To,Po,Tao])

def ddw(W,y0):
	# extract variables
	X = y0[0]
	T = y0[1]
	P = y0[2]
	Ta = y0[3]
	# Calculations
	# Kinetics
	k = 3600*np.exp(-176008/T-110.1*np.log(T)+912.8) # rate constant
	Kp = np.exp(42311/R/T) # equilibrium constant
	if X <= 0.05: #reaction rate < 5% conversion
		ra = k*(0.95/(thetas[2]+0.05))**0.5*(P/Po*Pao*(thetas[1]-0.025)/(1+epsilon*0.05)-((thetas[2]-0.05)/(1.05))**2*1/Kp**2)
	else: # reaction rate > 5% conversion
		ra = k*((1-X)/(thetas[2]+X))**0.5*(P/Po*Pao*(thetas[1]-0.5*X)/(1+epsilon*X)-((thetas[2]-X)/(1+X))**2*1/Kp**2)
	dXdW = ra/Fao # 
	# Energy
	dHr = -42471-1.563*(T-Tr)+1.36e-3*(T**2-Tr**2)-2459e-7*(T**3-Tr**3)
	flow_ratios = np.array([(thetas[0]-X),(thetas[1]-0.5*X),(thetas[2]+X),thetas[3]]) 
	A_pri = np.sum(A*flow_ratios) # flow-weighted A
	B_pri = np.sum(B*flow_ratios) # flow-weighted B
	C_pri = np.sum(C*flow_ratios) # flow-weighted C
	Cp = A_pri+B_pri*T+C_pri*T**2 # (theta*(Cp+XDCp))
	dTdW = (Ua*(Ta-T)+ra*dHr)/(Fao*(Cp)) # 
	dTadW = 0 # constant Ta
	# Pressure
	dPdW = alpha*(1-0.55*X)*T/P
	ddW = np.array([dXdW,dTdW,dPdW,dTadW])
	return ddW

W,Y = RKF45(ddw,0,100,y0)
print(Y)
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		