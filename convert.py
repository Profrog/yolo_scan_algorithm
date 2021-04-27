import serial
import time
import os
import string
import argparse
import cv2
import sys
import time
import math



data2 = open('data2.txt', 'r')
data3 = open('data3.txt', 'a')
data2.readline()
string0 = data2.readline()


while string0:
 data_list = string0.split(',')
 heading_data = (float(data_list[1])*180)/math.pi 
 
 line = "heading " + str(heading_data) + "\n"
 data3.write(line)
 
 data2.readline()
 string0 = data2.readline()
 
 ######3 other way
 
 # 해당 python 파일을 gnss 장비의 로그를 기록한 .txt 파일과 같이 둡니다.
# 로그 .txt 파일의 이름을 input.txt로 변형합니다
# linux 명령어 창에서 "python3 convert.py" 명령어를 통하여 본 프로그램을 실행하면 "output.txt"에 정리되어 나옵니다



data2 = open('input.txt', 'r')
data3 = open('output.txt', 'a')
#data2.readline()
string0 = data2.readline()

while string0:
 try: 
  data_list0 = string0.split('[')
  
  #output = str(float(linex[2])) + " " + str(float(liney[2])) + " " + str(float(linez[2])) + "\n"
  data_list00 = data_list0[2].split('}')
  
  linex = data_list00[0].split('"')
  liney = data_list00[1].split('"')
  linez = data_list00[2].split('"')
   
  output = str(float(linex[7])) + " " + str(float(liney[7])) + " " + str(float(linez[7])) + "\n"
  data3.write(output)
   
 except:
  print("error " + string0) 
  
  
 
 string0 = data2.readline()   

 
 ### more harder
 
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

 
 #### utm parsing
 
 
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
import utm
#from utm.conversion import from_latlon

# 해당 python 파일을 gnss 장비의 로그를 기록한 .txt 파일과 같이 둡니다.
# 로그 .txt 파일의 이름을 input.txt로 변형합니다
# linux 명령어 창에서 "python3 convert.py" 명령어를 통하여 본 프로그램을 실행하면 "output.txt"에 정리되어 나옵니다



data2 = open('LOG_RAILDRONE_UWB_BasePos.txt', 'r')
data3 = open('LOG_RAILDRONE_UWB_BasePos(out).txt', 'a')
#data2.readline()
string0 = data2.readline()

global output

while string0:
 try: 
 
  '''
  x_s = string0.find('posX')
  y_s = string0.find('posY')
  z_s = string0.find('posZ')
  
  s_length = 40 #string length
    
  stringx = string0[x_s:x_s + s_length]
  stringy = string0[y_s:y_s + s_length]
  stringz = string0[z_s:z_s + s_length] 
  ''' 
    
  linex = re.findall(r'(?<!\.)[-+]?\b\d+\.\d+(?!\.)\b', string0)
  #linex = re.findall(r'\d', string0)
  lat = linex[0]
  lon = linex[1]
  
   
  #output = str(lat)[2:len(str(linex)) - 2] + " " + str(lon)[2:len(str(liney)) - 2] + "\n"   
  u = utm.from_latlon(float(lat), float(lon))
  u1 = str(u)[1:len(str(u))-1].split(',')
  output = u1[0]  + u1[1] + "\n"
  data3.write(output)
  # print(linex) 
   
 except:
  print("error " + string0) 
  
  
 
 string0 = data2.readline()   

 
 
 
 
 
 
 
 
 
 
 
 
