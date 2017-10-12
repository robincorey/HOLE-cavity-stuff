from __future__ import print_function

import numpy as np
from scipy.integrate import simps
from numpy import trapz
import sys

filename = sys.argv[1]

#data, ydata = np.loadtxt(fname='%s' % filename, delimiter=',', usecols=(0,1), unpack=True)
xdata, ydata = np.loadtxt(fname='%s' % filename, delimiter=',', usecols=(0,1), unpack=True)
#Compute the area using the composite trapezoidal rule.
area = trapz(ydata, dx=0.5)
print("%s %s " % ( filename, area))
# Compute the area using the composite Simpson's rule.
#area = simps(ydata, dx=5)
#print("area =", area)
