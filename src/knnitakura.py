# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:49:37 2015

@author: Paco
"""

import numpy as np

'''
-----------------------
-- Distance feature
----------------------- 
'''
# Spectrum for Itakura measure
def amplitudeVector(x):
    resfft = np.fft.fft(x)
    return np.sqrt((resfft.real**2) + (resfft.imag**2))

ii = 0
def itakuraSaitoMetric(x,y):
    global ii
    print ii
    ii = ii + 1
    return np.sum(np.nan_to_num((x/y)-np.log(x/y)-1))

# TEST    
'''
dataset = loadData()
X2 = np.array([amplitudeVector(x[::60]) for x in dataset['X_train']])
knn = KNeighborsClassifier(n_neighbors=5, algorithm='ball_tree',metric='pyfunc', func=itakuraSaitoMetric)
knn.fit(X2,dataset['y_train'])
X3 = np.array([amplitudeVector(xx[::60]) for xx in dataset['X_test']])
pred = knn.predict(X3)
'''  
    