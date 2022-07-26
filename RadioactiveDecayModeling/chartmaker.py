# -*- coding: utf-8 -*-
"""
Created on Tue May 30 23:26:45 2017

@author: joseph hewitt
"""

from __future__ import division
import numpy as np
import pandas as pa
import matplotlib.pyplot as plt
from pylab import rcParams

rcParams['figure.figsize'] = 30,15

chart = pa.read_csv("./probable_decay.csv").values
print chart
print(len(chart))

for i in range(0,len(chart)):
    if chart[i,3] ==0:
        color = 'red'
    else:
        color = 'cyan'
    plt.hlines(chart[i,0],chart[i,1],chart[i,1]+1)
    plt.hlines(chart[i,0]+1,chart[i,1],chart[i,1]+1)
    plt.vlines(chart[i,1],chart[i,0],chart[i,0]+1)
    plt.vlines(chart[i,1]+1,chart[i,0],chart[i,0]+1)
    plt.text(chart[i,1],chart[i,0],chart[i,2],color=color)
    
plt.grid('on')
plt.show()