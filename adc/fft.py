import serial
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft


com12 = serial.Serial("com7", 115200)

if not com12.is_open:
  print("com12 open failed")
  exit()

print("等待串口")

fft_size =1024 #FFT处理的取样长度
txt = open("log.txt", "w")
y = []
for i in range(0, fft_size):
  string = com12.readline()
  txt.write(str(int(string)) + "\n")
  y.append(int(string))

com12.close()
txt.close()


x = []
for i in y:
    t = float(i)/4095*3.3
    x.append(t)
sampling_rate = 16000000/14 ##取样频率

xs=x[:fft_size]
xf = np.fft.rfft(xs)/fft_size # 
xf[0]=1e-6
xf[1]=1e-6
xf[2]=1e-6
#freqs = np.linspace(0, sampling_rate//2, fft_size//2+1)
freqs = range(0, fft_size//2)

xfp = 20*np.log10(np.clip(np.abs(xf),1e-20,1e1000))

plt.subplot(211)
plt.grid()
plt.plot(range(0, fft_size), y)
plt.title("origin")

plt.subplot(212)
plt.plot(freqs[0:511], xfp[0:511])
plt.title("fft")
plt.xlabel(u"kHz")
plt.subplots_adjust(hspace=0.4)

xf2=np.square(abs(xf))
Dc_Power=sum(xf2[0:2])
num=7   #采样的波形个数
sig=xf2[num] #有效信号，
noi_sndr=sum(xf2) - sig - Dc_Power;  # 包含谐波的噪声
n=xf2[num::num]   #谐波加基波
distortion=n[1:]  #谐波
noi_snr=np.sum(xf2)-np.sum(n) - Dc_Power   #噪声不包含谐波
snr=10*np.log10(sig)-10*np.log10(noi_snr)
sndr=10*np.log10(sig)-10*np.log10(noi_sndr)
thd=10*np.log10(np.sum(distortion))-10*np.log10(np.sum(n)); 
enob=(sndr-1.76)/6.02
print('snr ',snr)
print('sndr ',sndr)
print('thd ',thd)
print('enob ',enob)


#plt.get_current_fig_manager().window.showMaximized()
plt.show()
