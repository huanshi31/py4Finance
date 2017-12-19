# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:21:50 2017

@author: shihua
"""


a=100
type(a)
a.bit_length()
dir(a)




b=0.35
b+0.1
b.as_integer_ratio()

import decimal
from decimal import Decimal
decimal.getcontext().prec = 8
b=Decimal(35)/Decimal(100)+Decimal(.1)
b



import re
series = """
'01/18/2014 13:00:00', 100, '1st';
'01/18/2014 13:30:00', 110, '2nd';
'01/18/2014 14:00:00', 120, '3rd'
"""
dt = re.compile("'[0-9/:\s]+'")  # datetime
result = dt.findall(series)
result
from datetime import datetime
pydt = datetime.strptime(result[0].replace("'", ""),
                         '%m/%d/%Y %H:%M:%S')
pydt
print pydt
print type(pydt)