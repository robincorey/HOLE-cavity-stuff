from __future__ import print_function

import numpy as np
from scipy.integrate import simps
from numpy import trapz
import sys

def plotfunction ( str ):
        #filename = sys.argv[1]
        nuc = sys.argv[1]
       	half = sys.argv[2]
        filename = '%s/%s/%s_area.data' % ( nuc, i[j], half )
        #print '%s' % filename
        #data, ydata = np.loadtxt(fname='%s' % filename, delimiter=',', usecols=(0,1), unpack=True)
	xdata, ydata = np.loadtxt(fname='%s' % filename, delimiter=',', usecols=(0,1), unpack=True)
	#Compute the area using the composite trapezoidal rule.
	area = trapz(ydata, dx=0.5)
	print("%s %s %s =" % ( nuc, i[j], half ), area)
	# Compute the area using the composite Simpson's rule.
	#area = simps(ydata, dx=5)
	#print("area =", area)

i=[500, 502, 504, 506, 508, 510, 600, 602, 604, 606, 608, 610, 700, 702, 704, 706, 708, 710, 800, 802, 804, 806, 808, 810, 900, 902, 904, 906, 908, 910, 1000]
i=[1000, 502, 504, 506, 508, 510, 600, 602, 604, 606, 608, 700, 702, 704, 708, 802, 806, 808, 810, 902, 910]

for j in xrange(0, 31):
        plotfunction(j)
