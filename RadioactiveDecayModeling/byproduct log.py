# -*- coding: utf-8 -*-
"""
Created on Tue May 23 18:57:36 2017

@author: Hewitt
"""

from __future__ import division
import numpy as np
import pandas as pa

# Read user defined power, time, and composition
# [0,1]: power
# [1,1]: time in core
# [2-94,1]: moles of element x
data_in = pa.read_csv("./input_file").values
data_in_r, data_in_c = np.shape(data_in)
data_in_r = int(data_in_r)
data_in_c = int(data_in_c)
print(data_in)

# Isotope data initialization
# All stable isotopes are included
data = pa.read_csv("./temp_data").values
data_r, data_c = np.shape(data)
data_r = int(data_r)
data_c = int(data_c)
print(data)

# Calculate the % of each isotope in the sample
# mass of A times relative abundance of A-n
for i in range(2, data_in_r):
    for j in range(0,data_r):
        if data[j,0] == data_in[i,0]:
            data[j,3] = data_in[i,1]*data[j,2]
print(data)
print("%s%03d" %(data[10,0],data[10,1]))
