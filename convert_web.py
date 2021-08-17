import serial
import time
import os
import string
import argparse
import cv2
import sys
import time
import math
import re

# 해당 python 파일을 gnss 장비의 로그를 기록한 .txt 파일과 같이 둡니다.
# 로그 .txt 파일의 이름을 input.txt로 변형합니다
# linux 명령어 창에서 "python3 convert.py" 명령어를 통하여 본 프로그램을 실행하면 "output.txt"에 정리되어 나옵니다



data2 = open('input.txt', 'r')
data3 = open('output.txt', 'a')
#data2.readline()
string0 = data2.readline()

while string0:
 try: 
 
  x_s = string0.find('posX')
  y_s = string0.find('posY')
  z_s = string0.find('posZ')
  
  s_length = 40 #string length
    
  stringx = string0[x_s:x_s + s_length]
  stringy = string0[y_s:y_s + s_length]
  stringz = string0[z_s:z_s + s_length]  
    
  linex = re.findall(r'(?<!\.)[-+]?\b\d+\.\d+(?!\.)\b', stringx)
  liney = re.findall(r'(?<!\.)[-+]?\b\d+\.\d+(?!\.)\b', stringy)
  linez = re.findall(r'(?<!\.)[-+]?\b\d+\.\d+(?!\.)\b', stringz)
   
  output = str(linex)[2:len(str(linex)) - 2] + " " + str(liney)[2:len(str(liney)) - 2] + " " + str(linez)[2:len(str(linez)) - 2]  + "\n"   
  
  if str(linex)[2:len(str(linex)) - 2] != "":
   data3.write(output)
  # print(linex) 
   
 except:
  print("error " + string0) 
  
  
 
 string0 = data2.readline()   
