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

global tag1
tag1 = "DE"

global tag2
tag2 = "C0"

global tag3
tag3 = "55"

global tag4
tag4 = "5B"

global tag5
tag5 = "DD"

global tag6
tag6 = "C2"

global tag7
tag7 = "F4"

global tag8
tag8 = "F2"

def tag_checking(data):
 if data == tag1:
  return 1
 
 elif data == tag2:
  return 2

 elif data == tag3:
  return 3 

 elif data == tag4:
  return 4 

 elif data == tag5:
  return 5

 elif data == tag6:
  return 6

 elif data == tag7:
  return 7

 elif data == tag8:
  return 8

 else: 
  return 9

data2 = open('input.txt', 'r')
data3 = open('output.txt', 'a')
#data2.readline()
string0 = data2.readline()

while string0:
 try: 
  
  address_s = string0.find('address') 
  x_s = string0.find('posX')
  y_s = string0.find('posY')
  z_s = string0.find('posZ')
  at_s = string0.find('"at"')
  rssi_s = string0.find('rssi')
  
  s_length = 40 #string length

  string_address = string0[address_s:address_s + s_length]   
  stringx = string0[x_s:x_s + s_length]
  stringy = string0[y_s:y_s + s_length]
  stringz = string0[z_s:z_s + s_length]
  string_at = string0[at_s+3:at_s + s_length]
  string_rssi = string0[rssi_s : rssi_s + s_length]

  string_address_x = string_address.find('"',string_address.find('"')+1)
  string_address_y = string_address.find('"', string_address_x+2)
  string_address = string_address[string_address_x+1:string_address_y]
  string_address2 = string_address[len(string_address)-2:len(string_address)]

  string_at_x = string_at.find('"',string_at.find('"')+1)
  string_at_y = string_at.find('"', string_at_x+2)
  string_at = string_at[string_at_x+1:string_at_y]

  file_name = "output_" + str(tag_checking(string_address2)) + ".txt"
  data4 = open(file_name, 'a')
  #print(string_address)
  print("addrress is " + string_at)  
    
  linex = re.findall(r'(?<!\.)[-+]?\b\d+\.\d+(?!\.)\b', stringx)
  liney = re.findall(r'(?<!\.)[-+]?\b\d+\.\d+(?!\.)\b', stringy)
  linez = re.findall(r'(?<!\.)[-+]?\b\d+\.\d+(?!\.)\b', stringz)
  line_rssi = re.findall(r'(?<!\.)[-+]?\b\d+\.\d+(?!\.)\b', string_rssi)
   
  output = str(string_at) + " " + str(linex)[2:len(str(linex)) - 2] + " " + str(liney)[2:len(str(liney)) - 2] + " " + str(linez)[2:len(str(linez)) - 2]  + " " +  str(line_rssi)[2:len(str(line_rssi)) - 2]  +  "\n"   
  data4.write(output)
  data4.close()

  if str(linex)[2:len(str(linex)) - 2] != "":
   data3.write(output)
  # print(linex) 
   
 except:
  print("error " + string0) 
  
  
 
 string0 = data2.readline()   

