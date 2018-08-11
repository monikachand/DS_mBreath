import pyedflib
import numpy as np
import os
import pandas as pd

file_name = 'mesa-sleep-0001.edf'
full_file = os.path.abspath(os.path.join('data\\flow',file_name))

f = pyedflib.EdfReader(full_file)
n = f.signals_in_file
n1=f.getNSamples()[0]
signal_labels = f.getSignalLabels()

print(n1)
#print(f.readSignal(1))
print(signal_labels[8] ) # FLow variable
cols = ['Epoch','Flow']
df = pd.DataFrame(columns=cols)
#sigbufs = np.zeros((n, f.getNSamples()[0]))
data = []
data.append(f.readSignal(8))
data1 = [[]]
k=0
data = np.transpose(data)
print(data)
for i in range(0,len(data)):
    data1[i][0] = k
    data1[i][1] = data[i][0]
    k=k+0.03125

#lst= []
#lst.append(data)
print(data1[:10])
df = pd.DataFrame(np.array(data1),columns=cols)
#print(df)   
out_file =file_name+'.csv'  
df.to_csv(out_file,encoding='utf-8', index=False)
print("Output File "+out_file +' created....')