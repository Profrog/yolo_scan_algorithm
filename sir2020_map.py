import serial
import time
import os
import string
import argparse
import cv2
import sys
import time
import math
import numpy as np
import matplotlib.pyplot as plt



global size_a
size_a = 10000


global zoom
zoom = 30


def point_mark(x1,x2,y1,y2,data):    
 for x0 in range(x1,x2 +1,1):
   if x0 >= size_a: break
   for y0 in range(y1,y2 +1,1):
     if y0 >= size_a: break
     test1[x0,y0] = int(data) #after using other way  





test1 = np.zeros((size_a,size_a))

data2 =  open('data_map2.txt', 'r')
data3 = open('map_result.txt', 'a')
#data2.readline()
string0 = data2.readline()

while string0:
 
 data_list = string0.split(',')
 
 x = int((float(data_list[1]) * 10000)%10000)
 y = int((float(data_list[2]) * 10000)%10000)
 
 test1[x,y] = int(float(data_list[0]))
 point_mark(x-zoom,x+zoom,y-zoom,y+zoom,int(float(data_list[0])))
 
 print(str(x) + " " + str(y))
 
 
  
 string0 = data2.readline()
 
  
plt.matshow(test1);
plt.savefig('map_result.png', dpi=300)
plt.show() 
