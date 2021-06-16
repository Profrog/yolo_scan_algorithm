from pyzbar import pyzbar
from datetime import datetime
import argparse
import cv2
import sys
import time
import os
import sys
import subprocess
import signal
import numpy as np
import shutil
import pandas as pd

#test0

global search1
search1 = "folder_a"


if os.path.exists(search1):
 shutil.rmtree(search1) 

os.makedirs(search1)


global counter_a
counter_a = 0


global dir_coco
dir_coco = "cfg/custom.names"

global class_data
class_data = []

global max_counter
max_counter = 30


start2 = 0

net = cv2.dnn.readNet("working2.weights", "cfg/yolov4.cfg")
classes = []
with open(dir_coco, "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))



with open(dir_coco, "r") as f:
 for line in f.readlines():
  class_data.append(line[0:len(line) - 1])

# vc0 = cv2.VideoCapture(0)
#VideoCapture vc(0)
vc = cv2.VideoCapture(2) # 0은 노트북 웹캠 2는 usb로 연결된 웹캠
width, height = 1920, 1024

#vc.set(CV_CAP_PROP_FRAME_WIDTH,1920);
#vc.set(CV_CAP_PROP_FRAME_HEIGHT,1024);
#vc.set(CV_CAP_PROP_MODE, CV_CAP_MODE_YUYV);
#vc.set(CV_CAP_PROP_FPS, 60);


while counter_a < max_counter :
    #time.sleep(0.1)
    print("waiting...")
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    if True:
        print("webcam start!")
        start = time.time()
        chk = 0         
        vc.set(10,0.5)


        while counter_a <= max_counter :

            # ret0, frame0 = vc0.read()
            #cv2.imshow("Video Window0", frame0)  
            
            ret, frame = vc.read()
            cv2.imshow("Video Window", frame)   
            cv2.imwrite('image.jpg',frame)     

            image = cv2.imread('image.jpg')
            # image = cv2.resize(image, None, fx=0.4, fy=0.4)
            height, width, channels = image.shape
            
            barcodes = pyzbar.decode(image)
            
            blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
            net.setInput(blob)
            outs = net.forward(output_layers)
                  
            class_ids = []
            confidences = []
            boxes = []
            for out in outs:
             for detection in out:
              scores = detection[5:]
              class_id = np.argmax(scores)
              confidence = scores[class_id]
              if confidence > 0.5:
               class_data[class_id] += "," + str(confidence)
                          
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
               
               
               
            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)  
            font = cv2.FONT_HERSHEY_PLAIN
            for i in range(len(boxes)):
             if i in indexes:
              x, y, w, h = boxes[i]
              label = str(classes[class_ids[i]])
              color = colors[0]
            
              
              cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
              cv2.putText(image, label, (x, y + 30), font, 3, color, 3)
              cv2.imshow("Image", image)
              
            
              cv2.imwrite(search1 + "/image" + str(counter_a) + ".jpg",image) 
              counter_a += 1
             
       
            
            # os.system('./darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights image.jpg')
            # process = subprocess.Popen(..)   # pass cmd and args to the function
            # process.send_signal(signal.SIGINT)
            #global counter_a
            
            
           
                                        
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        
            #print(str(len(class_data)))
           
           
           
        df0 = open("export.txt" ,"w+")
        
        string_t = "yolo confidence data collection"
        for i in range(1,10*(max_counter + 1)):
         string_t += ",seq " + str(i) 
        
        string_t += "\n"
        
        df0.write(string_t)
        for i in range(0,len(class_data)):
         df0.write(class_data[i] + "\n")
           
           
            
        vc.release()
        cv2.destroyAllWindows()
        
        df0.close();

        df2_2 = pd.read_csv("export.txt",sep=",",encoding='utf-8')
        df2_2.to_excel('yolo_data.xlsx',index=False)
        
      
