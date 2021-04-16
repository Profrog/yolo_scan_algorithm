import serial
import time
import os
import string
import argparse
import cv2
import sys
import time
import math

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
