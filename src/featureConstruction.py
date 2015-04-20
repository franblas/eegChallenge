# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:08:49 2015

@author: Paco
"""

from signalprocessing import *
from fractal import *
from stats import *

def dictionaryInitialization():
    d = {'fft': list(), 
    'w0': list(), 
    'w1': list(), 
    'w2': list(), 
    'w3': list(), 
    'w4': list(), 
    'w5': list(), 
    'w6': list(), 
    'w7': list(), 
    'wc0': list(), 
    'wc1': list(), 
    'wc2': list(), 
    'wc3': list(), 
    'wc4': list(), 
    'wc5': list(), 
    'wc6': list(), 
    'wc7': list(), 
    'wr0': list(), 
    'wr1': list(), 
    'wr2': list(), 
    'wr3': list(), 
    'wr4': list(), 
    'wr5': list(), 
    'wr6': list(), 
    'wr7': list(), 
    'wb0': list(), 
    'wb1': list(), 
    'wb2': list(), 
    'wb3': list(), 
    'wb4': list(), 
    'wb5': list(), 
    'wb6': list(), 
    'wb7': list(),
    'ww0': list(), 
    'ww1': list(), 
    'ww2': list(), 
    'ww3': list(), 
    'ww4': list(), 
    'ww5': list(), 
    'ww6': list(), 
    'ww7': list(),
    'dfa': list(), 
    'pfd': list(), 
    'hfd': list(),
    'min': list(), 
    'max': list(), 
    'kurto': list(),
    'cwt': list(), 
    'fisher': list(),
    'autoco': list(),    
    'hjorth0': list(),
    'hjorth1': list(),
    'spentro': list(), 
    'svdentro': list(),  
    'p0': list(), 
    'p1': list(), 
    'p2': list(), 
    'p3': list()}
    return d

def waveletsAppend(x,d,dname='w',waveType='db8'):
    dd = d
    w = waveCoeffs(x,wave=waveType,levels=8)        
    dd[dname+'0'].append(w[0])     
    dd[dname+'1'].append(w[1]) 
    dd[dname+'2'].append(w[2]) 
    dd[dname+'3'].append(w[3]) 
    dd[dname+'4'].append(w[4])     
    dd[dname+'5'].append(w[5])
    dd[dname+'6'].append(w[6])
    dd[dname+'7'].append(w[7])
    return dd

'''
Super loop
'''
def dico_construction(X,dd):
    #X = dataset['X_train']
    d = dd
    for i in range(0,len(X)):
        #Signal processing 
        d['fft'].append(findFreq(X[i],fs=200,sel=10))       
        d = waveletsAppend(X[i],d,dname='w',waveType='db8')
        d = waveletsAppend(X[i],d,dname='wc',waveType='coif5')
        d = waveletsAppend(X[i],d,dname='wb',waveType='bior2.8')
        d = waveletsAppend(X[i],d,dname='wr',waveType='rbio2.8')
        d = waveletsAppend(X[i],d,dname='ww',waveType='sym8')
        d['cwt'].append(peakCWT(X[i]))
        d['autoco'].append(autoCorrelation(X[i]))
        
        #Fractal
        power_r = pyeegSignal(X[i])
        py_frac = pyeegFractal(X[i],pr=power_r)
        d['dfa'].append(py_frac[6])
        d['pfd'].append(py_frac[0])
        d['p0'].append(power_r[1][0])
        d['p1'].append(power_r[1][1])
        d['p2'].append(power_r[1][2])
        d['p3'].append(power_r[1][3])
        d['fisher'].append(py_frac[5])
        d['hjorth0'].append(py_frac[2][0])
        d['hjorth1'].append(py_frac[2][1])
        d['svdentro'].append(py_frac[4])
        d['hfd'].append(py_frac[1])
        d['spentro'].append(py_frac[3])
        
        #Stats
        stat = statsFeatures(X[i])
        d['min'].append(stat[0]) 
        d['max'].append(stat[1]) 
        d['kurto'].append(stat[2]) 
    return d
    
'''
do = dictionaryInitialization()
do = dico_train_construction(dataset['X_train'],do)

do_test = dictionaryInitialization()
do_test = dico_train_construction(dataset['X_test'],do_test)
'''
