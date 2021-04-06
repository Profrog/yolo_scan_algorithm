# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


import serial
import time
import os
import sys, time
import numpy as np
from scipy.ndimage import filters
import base64
import cv2
import io

from PIL import Image
from pyzbar import pyzbar
from datetime import datetime
import argparse
import time
import subprocess
import signal
import numpy as np
#yolo




# Ros libraries
#import roslib
#import rospy


def yolo():
 start2 = 0

 net = cv2.dnn.readNet("yolov4.weights", "cfg/yolov4.cfg")
 classes = []
 with open("cfg/coco.names", "r") as f:
     classes = [line.strip() for line in f.readlines()]
 layer_names = net.getLayerNames()
 output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
 colors = np.random.uniform(0, 255, size=(len(classes), 3))



 # vc0 = cv2.VideoCapture(0)
 vc = cv2.VideoCapture(0) # 0은 노트북 웹캠 2는 usb로 연결된 웹캠




 #time.sleep(0.1)
 print("waiting...")
     

 if True:
  print("webcam start!")
  start = time.time()
  chk = 0         
  vc.set(10,0.5)


  

  # ret0, frame0 = vc0.read()
  # cv2.imshow("Video Window0", frame0)  
      
  ret, frame = vc.read()
  cv2.imshow("Video Window", frame)  
      
  path1 = os.path.abspath('/home/mingyu/git_yolo/darknet/rosyolo2/ros2-vn300/dew_ws/image.jpg') 
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
       color = colors[i]
       cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
       cv2.putText(image, label, (x, y + 30), font, 3, color, 3)
       cv2.imshow("Image", image)
      
      # os.system('./darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights image.jpg')
      # process = subprocess.Popen(..)   # pass cmd and args to the function
      # process.send_signal(signal.SIGINT)
      

                              
    
  
  msg = String()
  msg.data = encode_img(image)
  # self.get_logger().info('vn_300 : "%s"' % msg.data)
  decode_img(msg.data)
       
  vc.release()
  cv2.destroyAllWindows()
  
  

  if chk == 1:
      print("access success")

  else:
      print("access failed")
  
  
  
def encode_img(img_fn):
 #img = cv2.imread(img_fn)
 img = img_fn
 jpg_img = cv2.imencode('.jpg', img)
 b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')  
 return b64_string
  

def decode_img(message):
 # fh = open("imageToSave.jpg", "wb")
 imgdata = base64.b64decode(str(message))
 image = Image.open(io.BytesIO(imgdata))
 image.save('image2.jpg')
 #cv2.imwrite('image2.jpg',image)
 
 #message_bytes = message.encode('ascii')
 #base64_bytes = base64.b64encode(message_bytes)
 # base64_message = base64_bytes.decode('ascii')
 # fh.write(base64_bytes)
 # fh.close()



def vn300(string):
	# print(string)
	global data_list
	data_list = string.decode().split(',')
	# double_list = map(double, data_list)
	# print(string)
	
	
	global Yaw_vn
	# Time_vn = data_list[1]
	Yaw_vn = data_list[4]
		
	global Pitch_vn
	Pitch_vn = data_list[5]
	
	global Roll_vn
	Roll_vn = data_list[6]
	
	global Latitude_vn	
	Latitude_vn = data_list[7]
	
	global Longitude_vn
	Longitude_vn = data_list[8]
	
	# Altitude_vn = data_list[9]
			
	# print("Time_vn " + Time_vn)
	# print("Yaw_vn " + Yaw_vn) 
	# print("Pitch_vn " + Pitch_vn)
	# print("Roll_vn " + Roll_vn)
	# print("Latitude_vn " + Latitude_vn)
	# print("Altitude_vn " + Altitude_vn)
	# print("---------------------------")


class MinimalPublisher(Node):



    def __init__(self):
        super().__init__('minimal_publisher')
        self.image_pub = self.create_publisher(String, 'vn_300', 10)   
        #self.subscription = self.create_subscription(String,'topic', self.showing,10)
               
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, yolo)
        self.i = 0
        
        
    def callback(self):
        '''Callback function of subscribed topic. 
        Here images get converted and features detected'''
       
        #### direct conversion to CV2 ####
        
        # with open('image.jpg','r', encoding = 'utf-16') as f:
         # img = f.read()
        
        # img = cv2.imread('image.jpg')     
        # np_arr = np.fromstring(img, np.uint8)
        
        # jpg_img = cv2.imencode('.jpg', img)
        # b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
                  
        # cv2.imshow('cv_img', img)
        # cv2.imwrite('image2.jpg',img) 

        #### Create CompressedIamge ####
        msg = String()
        # msg.header.stamp = 0
        # msg.format = "jpeg"
        #msg.data = np.array(cv2.imencode('.jpg', image_np)[1]).tostring()
        msg.data = encode_img('image.jpg')
        # print(msg.data)
        self.get_logger().info('vn_300 : "%s"' % msg.data)
        decode_img(msg.data)
        # Publish new image
        self.image_pub.publish(msg)        
        #self.subscriber.unregister()             
        # f.close()
              

    def timer_callback(self):
    
        vn300(ser.readline())	
        msg = String()
        msg.data = "\nRoll_vn : " + Roll_vn + "\nPitch_vn : " + Pitch_vn + "\nYaw_vn : " + Yaw_vn + "\n" + "\nLatitude : " + Latitude_vn + "\nLongitude : " + Longitude_vn + "\n"
        
        
                
        self.image_pub.publish(msg)
        self.get_logger().info('vn_300 : "%s"' % msg.data)
        self.i += 1
        
       


def main(args=None):
   
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
