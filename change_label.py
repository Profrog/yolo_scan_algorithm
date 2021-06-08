import os
import shutil
from pathlib import Path
from PIL import Image
from pyzbar import pyzbar
from datetime import datetime
import argparse
import time
import subprocess
import signal
import numpy as np
import re
import math
import serial
from scipy.ndimage import filters
import base64
import cv2
import io
import sys



global path
path = "working1/"

global search1
search1 = "working1a"


global dir_weights
dir_weights = 'yolov4.weights'


global dir_cfg 
dir_cfg = 'cfg/yolov4.cfg'

global dir_coco
dir_coco = 'cfg/coco.names'


global name_file
name_file = 'cfg/classes.txt'



if os.path.exists(search1):
 print("already has file")
 shutil.rmtree(search1)
 os.makedirs(search1) 

else:
 os.makedirs(search1)
 
 
print("찾을 label의 번호를 입력하시오")
o1 = int(input())

print("몇 번으로 바꾸시겠습니까?(번호입력)") 
n1 = int(input())
 
 
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".txt")]
search_num = 0

print ("file_list: {}".format(file_list_py)) 
 
for test1 in file_list_py:
  with open(path + test1) as file:
   if True:
    wr1 = open(search1 + "/" + test1, 'w+')
    for line in file.readlines():
     label_line = line.split(" ")
     if str(label_line[0]) == str(o1):
      search_num += 1
      label_dir = path + test1
      wr1_sen = line
      wr1_sen = wr1_sen.replace(str(o1),str(n1))
      wr1.write(wr1_sen)
      #print(wr1_sen)
      
     else:
      wr1.write(line) 
           
     #print("find label " + str(search_num) + "\n")
     shutil.copy(label_dir[0:len(label_dir) -4]  + ".jpg", search1)    
    
   #except:   
    #print("error in " + test1 + "\n")  
    #continue  
    


  
  
  
