import serial
import time
import os
import string
import argparse
import cv2
import sys
import time
import math


os.system("sudo chmod a+rw /dev/ttyUSB0")
global ser
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout = 1)
data =  open('data_map2.txt', 'w+')
ser.readline()
i = 0

while True:
 line_gng = ser.readline() #$GNGGA
 line_gph = ser.readline() #$GPHDT
 
 
 print(line_gph)
 
 gph_list = line_gph.decode().replace('\x00','').split(',')
 
 if gph_list[0] == '$GNGGA':  #except process
  a = line_gph
  line_gph = line_gng
  line_gng = a
  gph_list = line_gph.decode().replace('\x00','').split(',')

 
 
 #heading_data = (float(gph_list[1])*180)/math.pi 
 heading_data = float(gph_list[1])
 
 gng_list = line_gng.decode().replace('\x00','').split(',')
 latitude0 = gng_list[2]
 longitude0 = gng_list[4]
 line = str(heading_data) + "," + str(latitude0) + "," + str(longitude0) + "\n"
 
 print(line)
 data.write(line)
 time.sleep(0.01)
 #i = i + 1
data.close() 

"""
b'$GPHDT, 174.233,T*15\r\n'
b'$GNGGA,101905.69,3718.727361,N,12657.117765,E,1,08,1.0,73.5,M, 0.0, M,,0000*76\r\n'
b'$GPHDT, 174.246,T*17\r\n'
b'$GNGGA,101905.74,3718.727361,N,12657.117765,E,1,08,1.0,73.5,M, 0.0, M,,0000*7A\r\n'
"""



