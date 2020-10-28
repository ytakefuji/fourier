import numpy as np
from scipy.fftpack import fft
import pandas as pd
import numpy as np
data=pd.read_csv("d.csv")
import matplotlib.pyplot as plt
peak=200
y=data["us"][len(data)-peak:len(data)]
day=data['date'][len(data)-peak]
print(day)
N = len(y)
T = 4.0/N
x = T*np.arange(N)
yf = fft(y)
xf = 1/(N*T)*np.arange(N//2)
a=np.abs(yf[0:N//2]).astype(int)
a=sorted(a)
print(int(2.0/N*a[-4]))
#for i in a:
# print(int(2.0/N*i))

#plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
y=data["us"][0:len(data)]
x=np.arange(len(y))
plt.plot(len(data)-peak,y[len(data)-peak],'ro')
plt.plot(x, y)
plt.grid()
plt.show()
