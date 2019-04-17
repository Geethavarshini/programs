import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data=wav.read('voice.wav')
fs1,data1=wav.read('slow1.wav')
fs2,data2=wav.read('fast1.wav')
print(fs,fs1,fs2)
t1=np.arange(0,1.0/fs1)
t2=np.arange(0,1.0/fs2)
t1=np.arange(0,len(data)/fs1,1.0/fs)
t2=np.arange(0,len(data2)/fs2,1.0/fs)
print(data1,data2)
a1=plt.subplot(211)
a1.plot(t1,data[0:len(t1)])
a2=plt.subplot(212,sharex=a1)
a2.plot(t2,data[0:len(t2)])
plt.show()
