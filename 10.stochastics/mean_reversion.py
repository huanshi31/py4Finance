# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:41:48 2018

@author: shihua
"""
import numpy as np
import numpy.random as npr
from print_statistics import print_statistics

x0 = 0.05
kappa = 3.0
theta = 0.02
sigma = 0.1
T = 2.0
I = 10000
M = 50
dt = T / M

# Simulated square-root diffusion paths (Euler scheme)
def srd_euler():
    xh = np.zeros((M + 1, I))
    x1 = np.zeros_like(xh)
    xh[0] = x0
    x1[0] = x0
    for t in range(1, M + 1):
        xh[t] = (x1[t - 1]
              + kappa * (theta - np.maximum(x1[t - 1], 0)) * dt
              + sigma * np.sqrt(np.maximum(x1[t - 1], 0)) * np.sqrt(dt)  
              * npr.standard_normal(I))
        x1[t] = np.maximum(xh[t], 0)
    return x1
x1 = srd_euler()

# Simulated square-root diffusion at maturity (exact scheme)
def srd_exact():
    x2 = np.zeros((M + 1, I))
    x2[0] = x0
    for t in range(1, M + 1):
        df = 4 * theta * kappa / sigma ** 2
        c = (sigma ** 2 * (1 - np.exp(-kappa * dt))) / (4 * kappa)
        nc = np.exp(-kappa * dt) / c * x2[t - 1] 
        x2[t] = c * npr.noncentral_chisquare(df, nc, size=I)
    return x2
x2 = srd_exact()

print_statistics(x1[-1], x2[-1])