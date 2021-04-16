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
