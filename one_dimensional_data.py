#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 22:33:09 2017

@author: huanshi
"""

import numpy as np
#import matplotlib as mpl
import matplotlib.pyplot as plt

#%matplotlib inline

np.random.seed(1000)
y = np.random.standard_normal(20)
plt.plot(y)
v = (0.0, 20.0, -1.0, 1.0)
plt.axis(v)
plt.axis('scaled')


plt.figure(figsize=(7, 4))
plt.plot(y.cumsum(), 'b', lw=1.5)
plt.plot(y.cumsum(), 'ro')
#plt.plot(y.cumsum(), '--')
plt.grid(True)
plt.xlim(-1, 20)
plt.ylim(np.min(y.cumsum())-1, np.max(y.cumsum())+1)
#plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.title('A Simple Plot')