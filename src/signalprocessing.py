# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:07:11 2015

@author: Paco
"""

import numpy as np
import pandas as pd
from scipy import signal
from pyeeg import bin_power
import pywt

'''
-----------------------
-- Pyeeg features
-----------------------
'''
def pyeegSignal(X,fs=200,bb=[0.5,4,7,12,30]):
    return bin_power(X,Band=bb,Fs=fs)[1] 

'''
-------------------------
-- Frequencies features
-------------------------
'''
# Find the frequency of the signal
def findFreq(serie,fs=200,sel=10):
    fft0 = np.fft.rfft(serie*np.hanning(len(serie)))
    freqs = np.fft.rfftfreq(len(serie),d=1.0/fs)
    fftmod = np.array([np.sqrt(fft0[i].real**2 + fft0[i].imag**2) for i in range(0,len(fft0))])
    d = {'fft':fftmod,'freq':freqs}
    df = pd.DataFrame(d)
    hop = df.sort(['fft'],ascending=False)
    rows = hop.iloc[:sel]
    return rows['freq'].mean()

def whelchMethod(data,Fs=200):
    f, pxx = signal.welch(data, fs=Fs, nperseg=1024)
    d = {'psd': pxx, 'freqs': f}
    df = pd.DataFrame(data=d)
    dfs = df.sort(['psd'],ascending=False)
    rows = dfs.iloc[:10]
    return rows['freqs'].mean()

def butter_lowpass(cutoff, fs=200, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs=200, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = signal.lfilter(b, a, data)
    return y

'''
-----------------------
-- Wavelets features
-----------------------
'''
# Display all the wavelets available
def wavelist():
    for w in pywt.families():
        print pywt.wavelist(w)    


# DWT coeffs at level x
def waveCoeffs(data,wave='db4',levels=5):
    w = pywt.wavedec(data,wavelet=wave,level=levels)
    res = list()    
    for i in range(1,len(w)):
        temp = 0
        for j in range(0,len(w[i])):
            temp += w[i][j]**2
        res.append(np.sqrt(temp))    
    return res

def peakCWT(data):
    pics = signal.find_peaks_cwt(data,widths=np.arange(1,45),wavelet=signal.ricker)
    x = data[pics]
    n = np.linalg.norm(x)
    return n

'''
-----------------------
-- Signal features
-----------------------
'''
def autoCorrelation(data):
    return signal.correlate(data,data).mean()
