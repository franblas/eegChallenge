# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 12:24:16 2015

@author: Paco
"""

import numpy as np
from sklearn.cross_validation import train_test_split
from data import loadData
from featureConstruction import dictionaryInitialization,dico_construction
from models import listModels,createNormalizedDataframe,savePredictions

# Load datas
dataset = loadData()

# Train dictionary construction
d_train = dictionaryInitialization()
d_train = dico_construction(dataset['X_train'],d_train)
labels = np.array(dataset['y_train'])
Xarr_norm = createNormalizedDataframe(d_train)

# Test our models
X_train_train, X_train_test, y_train_train, y_train_test = train_test_split(Xarr_norm,labels,test_size=0.2,random_state=42)

X_train_train = np.nan_to_num(X_train_train)
X_train_test = np.nan_to_num(X_train_test)

# Scores
models = listModels()
for m in models:
    print m.get_params()
    m.fit(X_train_train,y_train_train)
    print m.score(X_train_test,y_train_test)

# Real training model
svc = models[len(listModels)-1].fit(Xarr_norm,labels)

# Test dictionary construction
d_test = dictionaryInitialization()
d_test = dico_construction(dataset['X_test'],d_test)
labels_t = np.array(dataset['y_test'])
Xarr_norm_t = createNormalizedDataframe(d_test)

# Prdecition of the model
pred_res = list()
for j in range(0,len(dataset['X_test'])):
    l = str(svc.predict(Xarr_norm_t[j])[0])
    pred_res.append(l)

# Write prediction into text file
savePredictions(pred_res)
