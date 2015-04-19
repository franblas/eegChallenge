# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:03:21 2015

@author: Paco
"""

import numpy as np
from scipy import io

'''
---------------------------------------------------
--- load eeg data
---------------------------------------------------
'''
def loadData(filename='data_challenge.mat'):
    return io.loadmat(filename)


'''
---------------------------------------------------
--- Save / Load python numpy arrays
---------------------------------------------------
'''
def saveBinaryMatrix(X,filename='datax.bin'):
    f = file(filename,'wb')
    np.save(f,X)
    f.close()
 
def loadBinaryMatrix(filename='dataX.bin'):
    f = file(filename,'rb')
    X = np.load(f)
    f.close()
    return X