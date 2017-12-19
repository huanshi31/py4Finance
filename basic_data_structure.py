# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 15:00:48 2017

@author: shihua
"""
#tuples
t = (1, 2.5, 'data')
type(t)
t[0]
type(t[2])
t.count('data')
t.index(1)
"""t[1] = 3.5 'tuple' object does not support item assignment"""


#list
l = [1, 2.5, 'data']
type(l)
l[0]
type(l[2])
l.count('data')
l.index(1)
l[1] = 3.5 
l  
"""list memeber could be changed"""
l.append([4, 3])
l
l.extend([1.0, 1.5, 2.0])  # append elements of list
l
l.insert(1, 'insert')  # insert object before index position
l
l.remove('data')  # remove first occurence of object
l
p = l.pop(3)  # removes and returns object at index
print l, p
l.reverse()
l
del l[-2]
l
l.sort()
l
m = [i ** 2 for i in range(5)]

""" filter map and reduce buit-in functions"""
m1 = map(lambda x: x**2, range(10))
m1
def even(x):
    return x % 2 == 0
m2 = filter(even, range(10))
m2
m3 = reduce(lambda x, y: x+y, range(10))
m3

#Dicts
"""Dicts are mutable too"""
d = {
     'Name' : 'Angela Merkel',
     'Country' : 'Germany',
     'Profession' : 'Chancelor',
     'Age' : 60
     }
type(d)
print d['Name'], d['Age']
d.keys()
d.values()
d.items()
birthday = True
if birthday is True:
    d['Age'] += 1
print d['Age']

for item in d.iteritems():
    print item
for value in d.itervalues():
    print type(value)

d2 = d.copy()
d2['Age'] = 40
d2['Name'] = "Anna"
del d2['Profession']
d2.popitem()
d2.clear()
d2

#Sets
"""unqilo but unorderd"""
s = set(['u', 'd', 'ud', 'du', 'd', 'du'])
s
type(s)
t = set(['d', 'dd', 'uu', 'u'])
s.union(t)  # all of s and t
s.intersection(t)  # both in s and t
s.difference(t)  # in s but not t
t.difference(s)  # in t but not s
s.symmetric_difference(t)  # in either one but not both

from random import randint
l = [randint(0, 10) for i in range(1000)]
    # 1,000 random integers between 0 and 10
len(l)  # number of elements in l
l[:20]
s = set(l)
s

























