# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 12:45:26 2018

@author: shihua
"""
import numpy as np
import numpy.random as npr
from  gen_sn import gen_sn

# pseudorandom 
print("%15s %15s" % ('Mean', 'Std. Deviation'))
print(31 * "-")
for i in range(1, 31, 2):
    npr.seed(1000)
    sn = npr.standard_normal(i ** 2 * 10000)
    print("%15.12f %15.12f" % (sn.mean(), sn.std()))

    
# improve first and second momentum
print("%15s %15s" % ('Mean', 'Std. Deviation'))
print(31 * "-")
for i in range(1, 31, 2):
    npr.seed(1000)
    sn = gen_sn(1, i ** 2 * int(10000), anti_paths=True, mo_match=True)
    print("%15.12f %15.12f" % (sn.mean(), sn.std()))