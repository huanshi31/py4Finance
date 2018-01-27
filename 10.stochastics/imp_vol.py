
# coding: utf-8

# In[1]:

V0 = 17.6639
r = 0.01
import pandas as pd
h5 = pd.HDFStore('vstoxx_data_31032014.h5', 'r')
futures_data = h5['futures_data']
options_data = h5['options_data']
h5.close()
futures_data


# In[2]:

options_data.info()
options_data[['DATE','MATURITY','TTM','STRIKE','PRICE']].head()


# In[14]:

options_data['IMP_VOL'] = 0.0
from bsm_functions import *
tol = 0.5  
for option in options_data.index:
    forward = futures_data[futures_data['MATURITY'] ==                 options_data.loc[option]['MATURITY']]['PRICE'].values[0]
    if (forward * (1 - tol) < options_data.loc[option]['STRIKE']
                             < forward * (1 + tol)):
        imp_vol = bsm_call_imp_vol(
                V0,  
                options_data.loc[option]['STRIKE'],
                options_data.loc[option]['TTM'],
                r,   
                options_data.loc[option]['PRICE'],
                sigma_est=2.,  
                it=100)
        options_data['IMP_VOL'].loc[option] = imp_vol


# In[15]:

options_data


# In[18]:

plot_data=options_data[options_data['IMP_VOL']>0]
maturities = sorted(set(options_data['MATURITY']))
maturities


# In[19]:

import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
plt.figure(figsize=(8, 6))
for maturity in maturities:
    data = plot_data[options_data.MATURITY == maturity]
      # select data for this maturity
    plt.plot(data['STRIKE'], data['IMP_VOL'],
             label=maturity.date(), lw=1.5)
    plt.plot(data['STRIKE'], data['IMP_VOL'], 'r.')
plt.grid(True) 
plt.xlabel('strike')
plt.ylabel('implied volatility of volatility')
plt.legend()
plt.show()


# In[28]:

keep = ['PRICE', 'IMP_VOL']
group_data = plot_data.groupby(['MATURITY', 'STRIKE'])[keep]
group_data = group_data.sum()
group_data.head()


# In[26]:

group_data.index.levels


# In[ ]:



