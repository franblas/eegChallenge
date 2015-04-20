# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:09:12 2015

@author: Paco
"""

import numpy as np
from pyeeg import *

'''
-----------------------
-- Pyeeg features
- pr : bin_power(X,Band=bb,Fs=fs)[1] 
-----------------------
'''
def pyeegFractal(X,fs=200,tau=4,dim=10,bb=[0.5,4,7,12,30],pr=list()):
    fod = first_order_diff(X)  
    r1 = pfd(X, D=fod)
    r2 = hfd(X, Kmax=5)
    r3 = hjorth(X, D=fod)
    r4 = spectral_entropy(X, Band=bb, Fs=fs, Power_Ratio=pr)
    r5 = svd_entropy(X, Tau=4, DE=dim)
    r6 = fisher_info(X, Tau=4, DE=dim)
    r7 = dfa(X)
    return r1,r2,r3,r4,r5,r6,r7


'''
-----------------------
-- Lyapunov exponent
-----------------------
'''
def d(series,i,j):
    return abs(series[i]-series[j])

def lyapunov(series,eps=1):
    res = list()
    N=len(series)
    dlist=[[] for i in range(N)]
    n=0 #number of nearby pairs found
    for i in range(N):
        for j in range(i+1,N):
            if d(series,i,j) < eps:
                n+=1
                #print n
                for k in range(min(N-i,N-j)):
                    dlist[k].append(np.log(d(series,i+k,j+k)))
    for i in range(len(dlist)):
        if len(dlist[i]):
            res.append(sum(dlist[i])/len(dlist[i]))  
    res = np.array(res)
    res2 = res[res!=-np.inf]        
    return res2        

'''
-----------------------
-- Correlation integral
-----------------------
'''
def heaviside(arr):
    return 0.5*(np.sign(arr)+1)
    
def correlationIntegral(data,eps=1):
    L = len(data)
    temp = 0.0
    for i in range(0,L):
        for j in range(i+1,L):
            if i!=j:
              temp += heaviside(eps - np.linalg.norm(data[i]-data[j]))  
    return (1./(L**2))*temp        
