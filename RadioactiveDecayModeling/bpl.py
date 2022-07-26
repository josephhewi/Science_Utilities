# -*- coding: utf-8 -*-
"""
Created on Wed May 31 20:25:36 2017

@author: Hewitt
"""

from __future__ import division
import numpy as np
import pandas as pa
import matplotlib.pyplot as plt
from pylab import rcParams
import time as t

rcParams['figure.figsize'] = 30,15

nuclides = pa.read_csv("./probable_decay.csv").values
datas = pa.read_csv("./test_input.csv").values
    
irradiation_time = datas[1,1]
power = datas[0,1]
time = 0 #indexing for tme
interval = 1 #time in seconds

"""
location    fast     thermal      gamma(rad/s)
CT         1.2e13     1.0e13      2.5e4
E-ring     6.4e12     4.1e12      1.5e4
F-ring     3.5e12     4.3e12      1.5e4
NEBP       2.0e12     2.0e12      1.0e4
RSR        1.5e12     1.8e12      4.0e3
rx|rf      1.1e11     3.4e11      -----
rxrf|      6.8e10     6.8e11      4.5e2
"""


flux_thermal = 1e13/250000*power
flux_fast = 1.2e13/250000*power


# distribute moles of input elements into their isotopes
for data in range(2,len(datas)):
    for nuclide in range(0,len(nuclides)):
        if ((datas[data,0]==nuclides[nuclide,2]) and (datas[data,1] != 0.0)):
            nuclides[nuclide,9]=nuclides[nuclide,3]/100*datas[data,1]*(6.022e23)
            print("{0}-{1}: {2}".format(nuclides[nuclide,2],nuclides[nuclide,1],nuclides[nuclide,9]))
        # ensure all zero-valued spaces are numerical zero
        for i in range(0,9):
            if (nuclides[nuclide,i] == "0"):
                nuclides[nuclide,i] = 0
        # additional variable reformatting 
        nuclides[nuclide,0] = int(nuclides[nuclide,0])
        nuclides[nuclide,1] = int(nuclides[nuclide,1])
        


while (time <= irradiation_time/interval):            
    for nuclide in range(0,len(nuclides)-1):
        A,Z,X,abundance,t_half,mode,gamma,s_th,s_res,N = nuclides[nuclide]
        s_th = s_th * 1e-24
        s_res = s_res * 1e-24
        if t_half == 0:
            decay_const = 0
        else:
            decay_const = 1/t_half
        dN_capture = round((N * (s_th * flux_thermal + s_res * flux_fast) * interval),0)
        dN_decay = round(((N * decay_const) * interval),0)
        dN = dN_decay + dN_capture 
        N = N - (dN_capture + dN_decay)
        nuclides[nuclide,9] = N
        nuclides[nuclide+1,9] = nuclides[nuclide+1,9] + dN_capture
        if ((mode != 0) and (dN_decay !=0)):
            #print("decay",dN)
            if mode == "B-":
                target_A = A+1
                target_Z = Z
            elif mode == "E":
                target_A = A-1
                target_Z = Z
            elif mode == "A":
                target_A = A-2
                target_Z = Z-4
            #print(target_A, target_Z)
            for i in range(0,(len(nuclides))):
                if ((nuclides[i,0] == target_A) and (nuclides[i,1] == target_Z)):
                    nuclides[i,9] = nuclides[i,9] + dN_decay
                    #print(nuclides[i,0],nuclides[i,1])
        #if N != 0:
        #   print("{0}{1}: {2},    {3}".format(X,Z,N,dN))
    time+=1
    #t.sleep(0.5)

    
    
for i in range(0,len(nuclides)):
    print(nuclides[i])
    #plt.scatter(nuclides[i,1],(nuclides[i,0]),np.log10(nuclides[i,9]))
    #plt.text(nuclides[i,0],np.log10(nuclides[i,9]),"{0}{1}".format(nuclides[i,2],nuclides[i,1]))
#plt.xlim(0,250)
#plt.ylim(0,95)    
#plt.show()

