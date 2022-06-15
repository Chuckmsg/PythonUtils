#！C:\Users\alp-sof\AppData\Local\Programs\Python\Python39\python.exe
import serial
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft


com = serial.Serial("com4", 115200)

if not com.is_open:
  print("com open failed")
  exit()

print("等待串口")

txt = open("log571k_div16_25.txt", "w")

#y = []
for i in range(0, 1000000):
  string = com.readline()
  txt.write(str(int(string)) + "\n")
  if (i % 10000) == 0:
    print("got " + str(i//10000) + "w values")
  #y.append(int(string))
print("done")

com.close()
txt.close()

input("输入回车结束")
