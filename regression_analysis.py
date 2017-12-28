#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 22:19:00 2017

@author: huanshi
"""
import numpy as np
import pandas as pd
from urllib import urlretrieve
import statsmodels.formula.api as smf

es_url = 'https://www.stoxx.com/document/Indices/Current/HistoricalData/hbrbcpe.txt'
vs_url = 'https://www.stoxx.com/document/Indices/Current/HistoricalData/h_vstoxx.txt'
urlretrieve(es_url, './data/es.txt')
urlretrieve(vs_url, './data/vs.txt')


cols = ['SX5P', 'SX5E', 'SXXP', 'SXXE', 'SXXF',
        'SXXA', 'DK5F', 'DKXF']
es = pd.read_csv(es_url, index_col=0, parse_dates=True,
                 sep=';', dayfirst=True, header=None,
                 skiprows=4, names=cols)
es.tail()

vs = pd.read_csv('./data/vs.txt', index_col=0, header=2,
                 parse_dates=True, dayfirst=True)
vs.info()

import datetime as dt
data = pd.DataFrame({'EUROSTOXX' :
                     es['SX5E'][es.index > dt.datetime(1999, 1, 1)]})
data = data.join(pd.DataFrame({'VSTOXX' :
                     vs['V2TX'][vs.index > dt.datetime(1999, 1, 1)]}))
    
data = data.fillna(method='ffill')
data2 = pd.DataFrame(data[data.index<dt.datetime(2015, 8, 8)])
data2.info()
data2.tail()
data2.plot(subplots=True, grid=True, style='b', figsize=(8, 6))
rets = np.log(data2 / data2.shift(1)) 
rets.head()
rets.plot(subplots=True, grid=True, style='b', figsize=(8, 6))

df=rets[1:][:]
model = smf.ols(formula="VSTOXX ~ EUROSTOXX", data=df).fit()
model.summary()
