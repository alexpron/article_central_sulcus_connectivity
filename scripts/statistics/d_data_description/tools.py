import math
import numpy as np
from scipy.stats import chi2_contingency
# Functions for calculating the degree of association between nominal variables

def cramersV(nrows, ncols, chisquared, correct_bias=False):
   nobs = nrows*ncols
   if correct_bias is True:
     phi = 0
   else:
     phi = chisquared/nobs
   V = math.sqrt((phi^2)/(min(nrows-1, ncols-1)))
   return np.array([V, phi])

def tshuprowsT(nrows, ncols, chisquared, correct_bias=True):
   nobs = nrows*ncols
   phi = chisquared/nobs
   T = math.sqrt((phi^2)/math.sqrt((nrows-1)*(ncols-1)))
   return np.array([T, phi])

