from time import time
from tkinter import Y
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

N = 1000   #1000
Fs=10000
Ts = 1/Fs
F=10
columns = np.genfromtxt("C:/Users/vinay/Desktop/Python Files/Sample.csv",delimiter=',')
time=columns[:,0]
Y = columns[:,1]
Amplitude = 1*np.sin(2*np.pi*F*Y)
plt.subplot(2,2,1),plt.plot(time,Amplitude,label="Amplitude",marker="*"),plt.legend(),plt.xlabel("Time(in Sec)"),plt.ylabel("Amplitude"),plt.grid(True)

AmplitudeFft = np.fft.fft(Amplitude)
AmplitudeMag = abs(AmplitudeFft)/len(time)

Freq = Fs/N
f = np.linspace(0,(N-1)*Freq, N)
Frequency = 1/time
plt.subplot(2,2,2),plt.plot(f,AmplitudeMag,label="Amplitude",marker="o"),plt.legend(),plt.xlabel("Time(in Sec)"),plt.ylabel("Amplitude"),plt.grid(True)
plt.subplot(2,2,3),plt.plot(Frequency,AmplitudeMag,label="Amplitude",marker="d"),plt.legend(),plt.xlabel("Time(in Sec)"),plt.ylabel("Amplitude"),plt.grid(True),plt.show()






