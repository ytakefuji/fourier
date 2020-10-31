#https://stackoverflow.com/questions/25735153/plotting-a-fast-fourier-transform-in-python
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Sample points
N= 400
# Sample spacing
T=1/(N+10)
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
p=2
xf = np.linspace(0.0, 1.0/(2.0*T),N//p)
plt.plot(xf, 1.0/N*np.abs(yf[0:N//p]))
plt.grid()
plt.show()
