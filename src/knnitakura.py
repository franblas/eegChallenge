# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:49:37 2015

@author: Paco
"""

import numpy as np
from scipy import signal
from sklearn.neighbors import KNeighborsClassifier


'''
-----------------------
-- Distance feature
----------------------- 
'''
# Spectrum for Itakura measure
def amplitudeVectorWelch(x,Fs=200):
    f, pxx = signal.welch(x, fs=Fs, nperseg=1024)
    return pxx

def itakuraSaitoMetric(x,y):
    return np.sum(np.nan_to_num((x/y)-np.log(x/y)-1))

# Model construction
def trainModel(X_train,y_train,neighbors=5):
    global ii
    ii = 0
    X2 = np.array([amplitudeVectorWelch(x[::60]) for x in X_train])
    model = KNeighborsClassifier(n_neighbors=neighbors, algorithm='ball_tree',metric='pyfunc', func=itakuraSaitoMetric).fit(X2,y_train)
    return model

def predict(knn,X_test):
    global ii
    ii = 0
    X3 = np.array([amplitudeVectorWelch(x[::60]) for x in X_test])
    pred = knn.predict(X3)
    return pred    

def vectorizeLabels(labs):
    res = list()
    ref = np.array(['W','R','N3','N2','N1'])
    for l in labs:
        res.append(np.where(ref==l.strip())[0][0])
    return res 

# TEST    
'''
dataset = loadData()
knn = trainModel(dataset['X_train'],dataset['y_train'])
res = predict(knn,dataset['X_test'])
ress = vectorizeLabels(res)
'''  
    