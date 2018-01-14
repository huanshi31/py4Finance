#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 10:49:17 2018

@author: huanshi
"""
clear

#The Zen of Python, by Tim Peters
import this  


# import * everything should be avoided for ambiguity
from math import *
log(10)

import math 
math.log(10)
# math.log? can be used to check documentation

import numpy as np
np.log(10)

#==============================================================================
# paradigm
#==============================================================================
loops = 25000

# 1: standard lib
from math import *
a = range(1, loops)
def f(x):
    return 3 * log(x) + cos(x) ** 2
%timeit r = [f(x) for x in a]

# 2: numpy is faster
import numpy as np
a = np.arange(1, loops)
%timeit r = 3 * np.log(a) + np.cos(a) ** 2

# 3: numexpr is fastest for numerical expressions
import numexpr as ne
ne.set_num_threads(4)
f = '3 * log(a) + cos(a) ** 2'
%timeit r = ne.evaluate(f)

