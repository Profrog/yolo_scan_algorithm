import serial
import time
import os
import string
import argparse
import cv2
import sys
import time


os.system("sudo chmod a+rw /dev/ttyUSB0")
global ser
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout = 1)
data =  open('data2.txt', 'a')

i = 0
while True:
 line = ser.readline()
 print(line)
 #print(i)
 data.write(line.decode("utf-8"))
 time.sleep(0.01)
 #i = i + 1


data.close() 



