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
from datetime import datetime


#test0


start2 = 0

net = cv2.dnn.readNet("yolov4.weights", "cfg/yolov4.cfg")
classes = []
with open("cfg/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))


#############
count = 0
attached = 0
before = 0
left_bound = 10
right_bound = 80
##############333

# vc0 = cv2.VideoCapture(0)
vc = cv2.VideoCapture(2) # 0은 노트북 웹캠 2는 usb로 연결된 웹캠


global data
data =  open('fish_logging.txt', 'a')



def checkbound(label,xs, xe):
     
     if(label != "car"):
      print("other object")
      return False

     elif xs >= left_bound and xs <= right_bound:
      print("Detect " + label)
      data.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')) + " " + label + " " + str(count) + "\n" )
      return True
    
     else: return False

while True :
    #time.sleep(0.1)
    print("waiting...")
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    if True:
        print("webcam start!")
        start = time.time()
        chk = 0         
        vc.set(10,0.5)


        while time.time() - start <= 300 :

            # ret0, frame0 = vc0.read()
            # cv2.imshow("Video Window0", frame0)  
            
            ret, frame = vc.read()
            cv2.imshow("Video Window", frame)   
            cv2.imwrite('image.jpg',frame)     
            image = cv2.imread('image.jpg')

            # image = cv2.resize(image, None, fx=0.4, fy=0.4)
            height, width, channels = image.shape
            left_bound = 1
            right_bound = int(width/6)

            
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
            attached = 0
            for i in range(len(boxes)):
             if i in indexes:
              x, y, w, h = boxes[i]
              label = str(classes[class_ids[i]])
              color = colors[i]
              cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
              cv2.putText(image, label, (x, y + 30), font, 3, color, 3)
              cv2.imshow("Image", image)
              if checkbound(label,x,x+w):
                attached += 1
            
            if(attached > before):
              count += attached - before
              print(count)
            before = attached
                
            # change option   
            cv2.rectangle(image, (left_bound,1), (right_bound, int(height)),(0,0,255), 3)
            cv2.imshow("Image", image)

 
                                          
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        vc.release()
        data.close()
        cv2.destroyAllWindows()

        if chk == 1:
            print("access success")

        else:
            print("access failed")


      
