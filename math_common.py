# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 16:37:10 2018

@author: shihua
"""
import numpy as np
#==============================================================================
# optimization
#==============================================================================
import scipy.optimize as spo

def fm((x, y)):
    return (np.sin(x) + 0.05 * x ** 2
          + np.sin(y) + 0.05 * y ** 2)

opt1 = spo.brute(fm, ((-10, 10.1, 0.1), (-10, 10.1, 0.1)), finish=None)
opt1
fm(opt1)

opt2 = spo.fmin(fm, opt1, xtol=0.001, ftol=0.001, maxiter=15, maxfun=20)
opt2
fm(opt2)

opt3 = spo.fmin(fm, (2.0, 2.0), maxiter=250)
opt3
fm(opt3)

# Constrained Optimization
def Eu((s, b)):
    return -(0.5 * np.sqrt(s * 15 + b * 5) + 0.5 * np.sqrt(s * 5 + b * 12))
#==============================================================================
# constraints : dict or sequence of dict, optional
# Constraints definition (only for COBYLA and SLSQP). Each constraint is defined in a dictionary with fields:
# type : str
# Constraint type: ‘eq’ for equality, ‘ineq’ for inequality.
# fun : callable
# Equality constraint means that the constraint function result is to be zero whereas inequality means that it is to be non-negative. Note that COBYLA only supports inequality constraints.
#==============================================================================
cons = ({'type': 'ineq', 'fun': lambda (s, b):  100 - s * 10 - b * 10})
  # budget constraint
bnds = ((0, 1000), (0, 1000))  # uppper bounds large enough

result = spo.minimize(Eu, [5, 5], method='SLSQP',
                       bounds=bnds, constraints=cons)

np.dot(result['x'], [10, 10])
#==============================================================================
# numerical integration
#==============================================================================
import scipy.integrate as sci
a = 0.5  # left integral limit
b = 9.5  # right integral limit
def f(x):
    return np.sin(x) + 0.5 * x
print sci.fixed_quad(f, a, b)[0] # gaussian quadrature
print sci.quad(f, a, b)[0] # adaptive quadrature
print sci.romberg(f, a, b) # romberg integration
xi = np.linspace(0.5, 9.5, 25) 
print sci.trapz(f(xi), xi) # take array, trapezoidal rule
sci.simps(f(xi), xi) # take array, simpson's rule

#==============================================================================
# symbolic fzero solver
#==============================================================================
import sympy as sy

x = sy.Symbol('x')
y = sy.Symbol('y')
z = 3 + sy.sqrt(x) - 4 ** 2
print sy.pretty(z)

f = x ** 2 + 3 + 0.5 * x ** 2 + 3 / 2
sy.simplify(f)

sy.solve(f)
sy.solve(x ** 2 + y ** 2)

#==============================================================================
# symbolic integration and differentiation
#==============================================================================
a, b = sy.symbols('a b')
print sy.pretty(sy.Integral(sy.sin(x) + 0.5 * x, (x, a, b)))

int_func = sy.integrate(sy.sin(x) + 0.5 * x, x)
print sy.pretty(int_func)
int_func.diff()
Fb = int_func.subs(x, 9.5).evalf()
Fa = int_func.subs(x, 0.5).evalf()
Fb - Fa

int_func_limits = sy.integrate(sy.sin(x) + 0.5 * x, (x, a, b))
print sy.pretty(int_func_limits)
int_func_limits.subs({a : 0.5, b : 9.5}).evalf()

sy.integrate(sy.sin(x) + 0.5 * x, (x, 0.5, 9.5))


f = (sy.sin(x) + 0.05 * x ** 2 + sy.sin(y) + 0.05 * y ** 2)
del_x = sy.diff(f, x)
del_y = sy.diff(f, y)
xo = sy.nsolve(del_x, -1.5)
yo = sy.nsolve(del_y, -1.5)
f.subs({x : xo, y : yo}).evalf() 
# global minimum