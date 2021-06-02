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
path = "t_image/"

global search1
search1 = "working2"


global dir_weights
dir_weights = 'yolov4.weights'


global dir_cfg 
dir_cfg = 'cfg/yolov4.cfg'

global dir_coco
dir_coco = 'cfg/coco.names'


global name_file
name_file = 'cfg/classes.txt'

global class_data
class_data = []




def yolo(original_image):           
        net = cv2.dnn.readNet(dir_weights, dir_cfg)
        classes = []
        with open(dir_coco, "r") as f:
            classes = [line.strip() for line in f.readlines()]
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        colors = np.random.uniform(0, 255, size=(len(classes), 3))
       
       
        print("waiting..." + original_image)
        
        
        if True:
         	                         
         image = cv2.imread(original_image)
         height, width, channels = image.shape
             
         #barcodes = pyzbar.decode(image)       
         blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False) #it about detect_size. check it 416*416
         net.setInput(blob)
         outs = net.forward(output_layers)
                   
         class_ids = []
         confidences = []
         boxes = []
         #print(str(height))
         
         with open(name_file, "r") as fileb:
          classes_find = [line.strip() for line in fileb.readlines()]
          
               
         for out in outs:
          for detection in out:
           
           scores = detection[5:]
           class_id = np.argmax(scores)
           confidence = scores[class_id]
           #print(str(detection))
           
           if confidence > 0.5:           
            # Object detected
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            
           
            class_data[class_id][1] += confidence*100
            class_data[class_id][2] += 1
            #print(class_data[class_id][1])
            
            # 좌표
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)
                                              
            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)  
            font = cv2.FONT_HERSHEY_PLAIN
            count = 0
          
                                                   
        #vc.release()
        cv2.destroyAllWindows()
        
     
 
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".jpg")]
search_num = 0

count = 0
with open(dir_coco, "r") as f:
 for line in f.readlines():
  class_data.append([line,float(0),float(0)])
  count += 1



df0 = open("export.txt" ,"w+")





print ("file_list: {}".format(file_list_py)) 
 
for test1 in file_list_py:
 #try: 
  yolo(path + test1)
             
 #except:   
  #print("error in " + test1 + "\n")  
  #continue



for i in range(0,len(class_data)):
 if class_data[i][2] > 0:
  df0.write(str(class_data[i][0])  + str(float(class_data[i][1])/float(class_data[i][2])) + "%" + "\n")

 else:
  df0.write(str(class_data[i][0])  +  str(float(0)) + "%" + "\n")


















  
  
  
  
    
