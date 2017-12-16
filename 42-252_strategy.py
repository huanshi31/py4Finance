#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
42-252_strategy.py
Created on Sat Dec 16 14:17:30 2017

@author: huanshi
"""

import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime


start = datetime.datetime(2000, 1, 1)
end = datetime.datetime(2014, 4, 14)

sp500 = web.DataReader("^GSPC", 'yahoo', start, end)
sp500.info()

sp500['Close'].plot(grid=True, figsize=(8,5))
sp500['42d']=np.round(pd.rolling_mean(sp500['Close'],window=42),2)
sp500['252d']=np.round(pd.rolling_mean(sp500['Close'],window=252),2)
sp500[['Close', '42d', '252d']].head()
sp500[['Close', '42d', '252d']].tail()
sp500[['Close', '42d', '252d']].plot(grid=True, figsize=(8,5))

sp500['42-252'] = sp500['42d'] - sp500['252d']
SD = 50
sp500['Regime'] = np.where(sp500['42-252']>SD, 1, 0)
sp500['Regime'] = np.where(sp500['42-252']<-SD, -1, sp500['Regime'])
sp500['Regime'].value_counts()

sp500['Regime'].plot(lw=1.5)
plt.ylim([-1.1,1.1])

sp500['Market'] = np.log(sp500['Close']/sp500['Close'].shift(1))
sp500['Strategy'] = sp500['Regime'].shift(1) * sp500['Market']
sp500['Strategy'].head()
sp500[['Market','Strategy']].cumsum().apply(np.exp).plot(grid=True,figsize=(8,5))
