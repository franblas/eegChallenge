# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:10:01 2015

@author: Paco
"""

import scipy.stats as stats

def statsFeatures(X):
    r1 = min(X)
    r2 = max(X)
    r3 = stats.kurtosis(X) 
    return r1,r2,r3
