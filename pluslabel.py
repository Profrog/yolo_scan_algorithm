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
path = "cam_train/"

global search1
search1 = "working2"


global dir_weights
dir_weights = 'weights/working2.weights'


global dir_cfg 
dir_cfg = 'cfg/yolov4.cfg'

global dir_coco
dir_coco = 'cfg/working2.names'


global name_file
name_file = 'cfg/custom.txt'



def yolo(label_a, original_image):
        label_t = open(label_a, 'a')       
        net = cv2.dnn.readNet(dir_weights, dir_cfg)
        classes = []
        with open(dir_coco, "r") as f:
            classes = [line.strip() for line in f.readlines()]
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        colors = np.random.uniform(0, 255, size=(len(classes), 3))
       
       
        print("waiting...")
        
        
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
           
           if confidence > 0.7:           
            # Object detected
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            
            # 좌표
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)
            
            for j in range(len(classes_find)):
             if(classes_find[j] == classes[class_id]):
              label_t.write(str(j) + " " + str(detection[0]) + " " + str(detection[1]) + " " + str(detection[2]) + " " + str(detection[3]) + "\n")
                
                       
            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)  
            font = cv2.FONT_HERSHEY_PLAIN
            count = 0
          
                                                   
        #vc.release()
        cv2.destroyAllWindows()
        label_t.close()
     




if os.path.exists(search1):
 print("already has file") 

else:
 os.makedirs(search1)
 
 
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".txt")]
search_num = 0

print ("file_list: {}".format(file_list_py)) 
 
for test1 in file_list_py:
 try:
  with open(path + test1) as file:
     label_dir = path + test1
     shutil.copy(label_dir, search1) 
     
     if label_dir.find(".xml") >= 0:
       label_dir2 = label_dir.replace(".xml","")
       data_file = Path(label_dir)
       data_file.rename(label_dir2)
       label_dir = label_dir2
              
     
     search_num += 1
     print("find dataset " + str(search_num) + "\n")
     #print(label_dir[0:len(label_dir) -4] + "\n")
     
     label_t = search1 + "/" + test1
     
     try:
      original_image = label_dir[0:len(label_dir) -4]  + ".jpg" 
      shutil.copy(label_dir[0:len(label_dir) -4]  + ".jpg", search1)
     except:
      try: 
       original_image = label_dir[0:len(label_dir) -4]  + ".jpeg" 
       shutil.copy(label_dir[0:len(label_dir) -4]  + ".jpeg", search1)
      except: 
       original_image = label_dir[0:len(label_dir) -4]  + ".png" 
       shutil.copy(label_dir[0:len(label_dir) -4]  + ".png", search1)
     
     
     yolo(label_t,original_image)
             
 except:   
  print("error in " + test1 + "\n")  
  continue




write_data = search1 + ".txt"  
filea = open(write_data, 'w+')
file_list2 = os.listdir(search1 + "/")  
file_list_py2 = [file for file in file_list2 if file.endswith(".txt")]  
print("all data_num is " + str(len(file_list_py2)) + "\n")   
filea.write("all data_num is " + str(len(file_list_py2)) + "\n")  
