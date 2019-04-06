# import the pyplot and wavfile modules

#Requiriments: install the python3-tk package

#                Ex: sudo apt-get install python3-pil.imagetk

import matplotlib.pyplot as plot
from matplotlib import mlab  # for csv2rec, detrend_none, window_hanning
from scipy.io import wavfile


# Read the wav file (mono)

samplingFrequency, signalData = wavfile.read('please.wav')

print(samplingFrequency)

# Plot the signal read from wav file

plot.subplot(211)

plot.title('Spectrogram of a wav file with piano music')

plot.plot(signalData)

plot.xlabel('Sample')

plot.ylabel('Amplitude')

plot.subplot(212)

signalMono = signalData[:,0]

#print(signalMono)

#plot.specgram(signalData, Fs=samplingFrequency)
plot.specgram(signalMono, NFFT=256, Fs=samplingFrequency, Fc=0, detrend=mlab.detrend_none,
         window=mlab.window_hanning, noverlap=128,
         cmap=None, xextent=None, pad_to=None, sides='default',
         scale_by_freq=None, mode='default', scale='default')

plot.xlabel('Time')

plot.ylabel('Frequency')

plot.show()