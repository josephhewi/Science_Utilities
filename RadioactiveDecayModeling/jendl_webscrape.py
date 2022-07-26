# -*- coding: utf-8 -*-
"""
Created on Mon May 22 22:51:18 2017

@author: Hewitt
"""

from __future__ import division
import numpy as np
import pandas as pa
from lxml import html
import requests as rq

start_row=0
start_col=0

# get list of isotopes using pandas
data = pa.read_csv("JENDL_index.csv").values
x,y = np.shape(data)
print(x,y)

# loop through isotopes, scraping from JENDL
for i in range(start_row,x):
    for j in range(start_col,y):
        if (data[i,j] != "0"):
            print(data[i,j], i, j)
            page = rq.get("http://wwwndc.jaea.go.jp/cgi-bin/UNZIP_jendl.cgi?lib=J40P3&iso={0}".format(data[i,j]))
            tree = html.fromstring(page.content)
            isotope = open("./Repository/{0}_JENDL.info".format(data[i,j]),"w+")
            isotope.write("{0}\n".format(data[i,j]))
            isotope.write(tree.text)
            isotope.close()
