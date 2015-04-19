# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:49:37 2015

@author: Paco
"""

import numpy as np
from sklearn.neighbors import KNeighborsClassifier


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

# Model construction
def trainModel(X_train,y_train,neighbors=5):
    global ii
    ii = 0
    X2 = np.array([amplitudeVector(x[::60]) for x in X_train])
    model = KNeighborsClassifier(n_neighbors=neighbors, algorithm='ball_tree',metric='pyfunc', func=itakuraSaitoMetric).fit(X2,y_train)
    return model

def predict(knn,X_test):
    global ii
    ii = 0
    X3 = np.array([amplitudeVector(x[::60]) for x in X_test])
    pred = knn.predict(X3)
    return pred    

# TEST    
'''
dataset = loadData()
knn = trainModel(dataset['X_train'],dataset['y_train'])
res = predict(knn,dataset['X_test'])
'''  
    