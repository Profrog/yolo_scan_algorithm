
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
left_bound = 0
right_bound = 0
fishbowlsize = 0.25
bowl_left = 0
bowl_right = 0
isDragging = False
x0, y0, w, h = -1, -1, -1, -1
blue, red, black = (255, 0, 0), (0, 0, 255), (0, 0, 0)
meter_rate = 1
left_frame = 0
right_frame = 0
##############333

# vc0 = cv2.VideoCapture(0)
vc = cv2.VideoCapture(2) # 0은 노트북 웹캠 2는 usb로 연결된 웹캠
#vc = cv2.VideoCapture('/home/kjjgo35/PythonHome/darknet/test.mkv')


global data
data =  open('fish_logging.txt', 'a')

def onMouse(event, x, y, flags, param):
    global isDragging, x0, y0, img, left_bound, right_bound, height, name, meter_rate, bowl_left, bowl_right
    if event == cv2.EVENT_LBUTTONDOWN:
        isDragging = True
        x0 = x
        y0 = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if isDragging:
            img_draw = img.copy()
            cv2.rectangle(img_draw, (x0, y0), (x, y), blue, 2)
            cv2.imshow(name, img_draw)
    elif event == cv2.EVENT_LBUTTONUP:
        if isDragging:
            isDragging = False
            w = x - x0
            h = y - y0
            if w > 0 and h > 0:
                img_draw = img.copy()
                img_draw2 = img.copy()
                cv2.rectangle(img_draw, (x0, y0), (x, y), red, 2)
                cv2.imshow(name, img_draw)
                roi = img_draw[y0:y0+h, x0:x0+w]
                #cv2.imshow('cropped', roi)
                cv2.imshow(name, img_draw)
                #cv2.moveWindow('cropped', 0, 0)
                #cv2.imwrite('./cropped.png', roi)
                if name == 'mirror':
                    left_bound = x0
                    right_bound = x
                    print(left_bound, right_bound)
                    cv2.rectangle(img_draw2, (left_bound,1), (right_bound, int(height)),(0,0,255), 3)
                elif name == 'bowl':
                    bowl_left = x0
                    bowl_right = x
                    print(bowl_left, bowl_right)
                    cv2.rectangle(img_draw2, (bowl_left,1), (bowl_right, int(height)),(0,0,255), 3)
                    meter_rate = fishbowlsize /(bowl_right - bowl_left)
                font = cv2.FONT_HERSHEY_PLAIN
                cv2.putText(img_draw2, name, (x0, 40), font, 3, black, 3)
                cv2.imshow(name, img_draw2)
            else:
                cv2.imshow(name, img)
                print('drag should start from left-top side')


def checkbound(label,xs, xe):
     
     if(label != "zebra fish"):
      print("other object")
      return False

     elif xs >= left_bound and xs <= right_bound:
      print("Detect " + label)
      data.write(str(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')) + " " + label + " " + str(count) + "\n" )
      return True
    
     else: return False

def checkframe():
    global left_frame,right_frame,bowl_left,bowl_right,left_bound,right_bound
    bowl_size = bowl_right - bowl_left
    left_frame = left_bound
    right_frame = right_bound
    if bowl_left < left_bound :
        left_frame = left_bound - (bowl_size / 5)
    if bowl_right > right_bound :
        right_frame = right_bound + (bowl_size / 5)


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

        ret,frame = vc.read()
        cv2.imshow("Video Window", frame)
        cv2.imwrite('selectroi.jpg',frame)
        img = cv2.imread('selectroi.jpg')
        name = 'mirror'
        cv2.imshow(name,img)
        print("Set the mirror and press any key")
        height, width, channels = img.shape
        cv2.setMouseCallback(name,onMouse)
        print(left_bound,',', right_bound)
        cv2.waitKey()
        cv2.destroyWindow(name)

        name = 'bowl'
        cv2.imshow(name,img)
        print("Set the bowl and press any key")
        cv2.setMouseCallback(name,onMouse)
        print(left_bound,',', right_bound)
        cv2.waitKey()
        cv2.destroyWindow(name)

        checkframe()
        print("lf = " , left_frame, right_frame)

        while time.time() - start <= 300 :

            # ret0, frame0 = vc0.read()d
            # cv2.imshow("Video Window0", frame0)  
            
            ret, frame = vc.read()
            cv2.imshow("Video Window", frame)
            cv2.imwrite('image.jpg',frame)
            image = cv2.imread('image.jpg')
            cv2.imshow("Image", image)
            
            # image = cv2.resize(image, None, fx=0.4, fy=0.4)
            height, width, channels = image.shape
            #left_bound = 1
            #right_bound = int(width/6)

            
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
               #if center_x < left_frame or center_x > right_frame :
                #   continue
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
              x += w//20
              y += h//20
              w -= w//20
              h -= h//20
              if x + w <= left_bound :
                distance = str(round((left_bound - x - w) * meter_rate,3))
              elif x >= right_bound : 
                distance = str(round((x - right_bound) * meter_rate, 3))
              else :
                distance = "0"
              label = str(classes[class_ids[i]])
              color = colors[i]
              cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
              cv2.putText(image, label, (x, y + 30), font, 3, color, 3)
              cv2.putText(image, distance , (x, y - 30), font, 3, color, 3)
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
