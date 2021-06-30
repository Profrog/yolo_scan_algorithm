import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from custom_msg.msg import DataA

import serial
import numpy as np
import time
import os

global dataB
dataB = open('direct.txt', 'r')

class DataAPublisher(Node):


    def __init__(self,Hz):
        super().__init__('DataA_publisher')
        self.frame_id = 'DataA'
        self.publisher_ = self.create_publisher(DataA, self.frame_id , 1)
        timer_period = 1/(Hz*2)  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)


    def DataA(self, string):
        data_list = string.split(',') 
        return data_list
        

    def timer_callback(self):
        serialBuffer = dataB.readline()
        msgList = self.DataA(serialBuffer)
        
        if len(msgList) < 1:
            self.get_logger().info('데이터가 부족합니다. ')
        else:    
            msg = DataA()
            logString = ("\nx_dir : " + msgList[0] + "\ny_dir : " + msgList[1]
                         + "\nspeed : " + msgList[2] + "\n")
                                             
            msg.x_dir = float(msgList[0])             
            msg.y_dir = float(msgList[1])
            msg.speed = float(msgList[2])             
                        
            # pup msg
            self.publisher_.publish(msg)
            self.get_logger().info('dataA : --- "%s"' % logString)
                     

def main(args=None):

    rclpy.init(args=args)
    DataA_publisher = DataAPublisher(40) # sensor rate는 여기에
    rclpy.spin(DataA_publisher)

    DataA_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
