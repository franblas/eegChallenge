# -*- coding: utf-8 -*-
"""
Created on Fri Apr 03 20:49:00 2015

@author: Paco
"""

'''
training
'''
print "begin training"
#labs = list()
#d = {'hann': list(), 'hamm': list(), 'black': list(), 'w0': list(), 'w1': list(), 'w2': list(), 'w3': list(), 'w4': list(), 'w5': list(), 'w6': list(), 'w7': list(), 'dfa': list(), 'pfd': list(), 'p0': list(), 'p1': list(), 'p2': list(), 'p3': list()}
#d['fft'] = list()
for i in range(0,len(dataset['X_train'])):
    '''
    label = str(dataset['y_train'][i])
    w = waveCoeffs(dataset['X_train'][i],wave='db8',levels=8)
    d['hann'].append(meanFFT(dataset['X_train'][i],'hanning'))  
    d['hamm'].append(meanFFT(dataset['X_train'][i],'hamming'))
    d['black'].append(meanFFT(dataset['X_train'][i],'black'))   
    d['w0'].append(w[0])     
    d['w1'].append(w[1]) 
    d['w2'].append(w[2]) 
    d['w3'].append(w[3]) 
    d['w4'].append(w[4])     
    d['w5'].append(w[5])
    d['w6'].append(w[6])
    d['w7'].append(w[7])   
    fdiff = pyeeg.first_order_diff(dataset['X_train'][i])
    fdiff.append(0.0)
    d['dfa'].append(pyeeg.dfa(dataset['X_train'][i],fdiff))
    d['pfd'].append(pyeeg.pfd(dataset['X_train'][i],fdiff))
    pratio = pyeeg.bin_power(dataset['X_train'][i],[0.5,4,7,12,30],200)[1]
    d['p0'].append(pratio[0])
    d['p1'].append(pratio[1])
    d['p2'].append(pratio[2])
    d['p3'].append(pratio[3])
    d['fisher'].append(pyeeg.fisher_info(dataset['X_train'][i],4,10))
    d['hjorth0'].append(pyeeg.hjorth(dataset['X_train'][i])[0])
    d['hjorth1'].append(pyeeg.hjorth(dataset['X_train'][i])[1])
    '''
    #rbio2.8,bior2.8,sym8
    '''
    ww = waveCoeffs(dataset['X_train'][i],wave='coif5',levels=8)
    d['wc0'].append(ww[0])     
    d['wc1'].append(ww[1]) 
    d['wc2'].append(ww[2]) 
    d['wc3'].append(ww[3]) 
    d['wc4'].append(ww[4])     
    d['wc5'].append(ww[5])
    d['wc6'].append(ww[6])
    d['wc7'].append(ww[7]) 
    d['cwt'].append(peakCWT(dataset['X_train'][i]))
    d['svdentro'].append(pyeeg.svd_entropy(dataset['X_train'][i],4,10))
    d['min'].append(min(dataset['X_train'][i])) 
    d['max'].append(max(dataset['X_train'][i])) 
    d['kurto'].append(stats.kurtosis(dataset['X_train'][i])) 
    d['hfd'].append(pyeeg.hfd(dataset['X_train'][i],5))
    
    hop = list()
    hop.append(d['p0'][i])
    hop.append(d['p1'][i])
    hop.append(d['p2'][i])
    hop.append(d['p3'][i])
    d['spentro'].append(pyeeg.spectral_entropy(dataset['X_train'][i],Band=[0.5,4,7,12,30],Fs=200,Power_Ratio=hop))
    '''    
    #d['hurst'].append(pyeeg.hurst(dataset['X_train'][i]))
    d['fft'].append(findFreq(dataset['X_train'][i]))
    #labs.append(label)
labels = np.array(labs)
df = pd.DataFrame(data=d)
df_norm = (df - df.mean()) / df.std()
Xarr_norm = np.array(df_norm)

'''
test classifier
'''
print "begin test"
#d_t = {'hann': list(), 'hamm': list(), 'black': list(), 'w0': list(), 'w1': list(), 'w2': list(), 'w3': list(), 'w4': list(), 'w5': list(), 'w6': list(), 'w7': list(), 'dfa': list(), 'pfd': list(), 'p0': list(), 'p1': list(), 'p2': list(), 'p3': list()}
#d_t['autoco'] = list()
for i in range(0,len(dataset['X_test'])):
    '''
    w = waveCoeffs(dataset['X_test'][i],wave='db8',levels=8)
    d_t['hann'].append(meanFFT(dataset['X_test'][i],'hanning'))  
    d_t['hamm'].append(meanFFT(dataset['X_test'][i],'hamming'))
    d_t['black'].append(meanFFT(dataset['X_test'][i],'black'))
    d_t['w0'].append(w[0])     
    d_t['w1'].append(w[1]) 
    d_t['w2'].append(w[2]) 
    d_t['w3'].append(w[3]) 
    d_t['w4'].append(w[4]) 
    d_t['w5'].append(w[5])
    d_t['w6'].append(w[6])
    d_t['w7'].append(w[7])   
    fdiff_t = pyeeg.first_order_diff(dataset['X_test'][i])
    fdiff_t.append(0.0)
    d_t['dfa'].append(pyeeg.dfa(dataset['X_test'][i],fdiff_t))
    d_t['pfd'].append(pyeeg.pfd(dataset['X_test'][i],fdiff_t))
    pratio_t = pyeeg.bin_power(dataset['X_test'][i],[0.5,4,7,12,30],200)[1]
    d_t['p0'].append(pratio_t[0])
    d_t['p1'].append(pratio_t[1])
    d_t['p2'].append(pratio_t[2])
    d_t['p3'].append(pratio_t[3])
    d_t['hjorth0'].append(pyeeg.hjorth(dataset['X_test'][i])[0])
    d_t['hjorth1'].append(pyeeg.hjorth(dataset['X_test'][i])[1])
    pratio = pyeeg.bin_power(dataset['X_test'][i],[0.5,4,7,12,30],200)[1]
    d_t['p0'].append(pratio[0])
    d_t['p1'].append(pratio[1])
    d_t['p2'].append(pratio[2])
    d_t['p3'].append(pratio[3])
    d_t['fisher'].append(pyeeg.fisher_info(dataset['X_test'][i],4,10))
    d_t['cwt'].append(peakCWT(dataset['X_test'][i]))
    d_t['svdentro'].append(pyeeg.svd_entropy(dataset['X_test'][i],4,10))
    d_t['min'].append(min(dataset['X_test'][i])) 
    d_t['max'].append(max(dataset['X_test'][i])) 
    d_t['kurto'].append(stats.kurtosis(dataset['X_test'][i])) 
    d_t['hfd'].append(pyeeg.hfd(dataset['X_test'][i],5))
    hop = list()
    hop.append(d_t['p0'][i])
    hop.append(d_t['p1'][i])
    hop.append(d_t['p2'][i])
    hop.append(d_t['p3'][i])
    d_t['spentro'].append(pyeeg.spectral_entropy(dataset['X_test'][i],Band=[0.5,4,7,12,30],Fs=200,Power_Ratio=hop))
    d_t['autoco'] = autoCorrelation(dataset['X_test'][i][::2])
    '''
    
df_t = pd.DataFrame(data=d_t)
df_t_norm = (df_t - df_t.mean()) / df_t.std()
Xarr_t_norm = np.array(df_t_norm)

print "end of test"
