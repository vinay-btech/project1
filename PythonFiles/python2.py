import scipy.fft
import matplotlib.pyplot as plt
import numpy as np


N = 500
T = 1.0 / 600.0
x = np.linspace(0.0, N*T, N)
y = np.sin(60.0 * 2.0*np.pi*x) + 0.5*np.sin(90.0 * 2.0*np.pi*x)
y_f = scipy.fft.fft(y)
x_f = np.linspace(0.0, 1.0/(2*T), N//2)

print(x_f)
print(x)
#print(abs(x_f))
print(len(x_f))
#print(len(y_f[:N//2]))
print(len(x))
#print(len(y))
#plt.plot(x_f,y_f),plt.grid(),plt.show()
#plt.subplot(2,1,1)
#plt.plot(x,y),plt.grid(True)
#plt.subplot(2,1,2)
#plt.plot(x_f, 2.0/N * np.abs(y_f[:N//2])),plt.grid()
#plt.show()
#plt.plot(x_f,abs(y_f[:N//2])),plt.grid(),plt.show()