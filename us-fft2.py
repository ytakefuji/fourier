import numpy as np
from scipy.fftpack import fft
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("d.csv")
import matplotlib.pyplot as plt
y=data["us"][0:238]
x=np.arange(238)
#plt.plot(x,y)
day=180
print(data['date'][120])
#plt.plot(day,y[day],'ro')
y=data["us"][day:238]
N = len(y)
T = 4.0/N
x = T*np.arange(N)
yf = fft(y)
xf = 1/(N*T)*np.arange(N//2)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]),'r')
y=data["us"][0:day]
N = len(y)
T = 4.0/N
x = T*np.arange(N)
yf = fft(y)
xf = 1/(N*T)*np.arange(N//2)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]),'b')
plt.grid()
plt.legend(('after:'+str(day)+'th','before:'+str(day)+'th'))
plt.show()
