#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 09:48:17 2018

@author:alper
"""

import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt("team.csv", delimiter=",", dtype=None, encoding="iso-8859-1")[1:]
x = data[:, 4].astype(np.float)
y = data[:, 6].astype(np.float)


def slope_intercept (x_val,y_val):
    x=np.array(x_val)
    y=np.array(y_val)
    m=(((np.mean(x)*np.mean(y))-np.mean(x*y))/((np.mean(x)*np.mean(x))-np.mean(x*x)))
    m=round(m,2)
    b=(np.mean(y)-np.mean(x)*m)
    b=round(b,2)
    return m,b
m,b=slope_intercept(x,y)
reg_line=[(m*x)+ b for x in x]
plt.scatter(x,y)
plt.plot(x,reg_line,color="blue")
plt.ylabel("Experience")
plt.xlabel("Age")
plt.show()