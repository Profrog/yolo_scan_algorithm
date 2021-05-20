from PIL import Image
import os
import time
import urllib.request
import urllib
import socket
import shutil

import time
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait




#global time_limit
#time_limit = 15
#socket.setdefaulttimeout(time_limit)


global n #num of case
n = 10

global url0
url0 = "https://www.google.co.kr/imghp?hl=ko&ogbl"

global file_name
file_name = 't_image'

if os.path.exists(file_name):
 shutil.rmtree(file_name) 

os.makedirs(file_name)


print("검색할 커맨드를 입력하시오")
search1 = input()

data2 = open('crol_box.txt' , 'w+') #web code
driver = webdriver.Chrome()
driver.get(url = url0)
elem = driver.find_element_by_name("q")
elem.send_keys(search1)
elem.send_keys(Keys.RETURN)

data2.write(driver.page_source)
data2.close()


print("몇 개를 검색하시겠습니까")
n = int(input())
driver.close()

data3 = open('crol.txt', 'w+') # link configz
data4 = open('error_link.txt', 'w+')
train0 = open('train.txt', 'w+') #train_txt
i = 1


while i <= n:
 with open('crol_box.txt') as file:
    for line in file.readlines():
     try:
      if i > n:
       break
    
      if line.find('.jpg"')== -1:
       continue
     
      else:  
       a = line.find('.jpg"') + 5
       b = line.find('"h')
       str0 = line[b:a]
       str1 = str0[1:len(str0) -1]
       #print(str1)
       data3.write(str1 + "\n")
       urllib.request.urlretrieve(str1, file_name + "/test" + str(i) + '.jpg')
       train0.write(file_name + str(i) + '.jpg' + "\n")  
       i+=1
           
     except:
      print("error " + str1)
      data4.write(str1 + "\n")
      i-=1
      continue
  
 if i <= n:
  data2 = open('crol_box.txt' , 'w+') #web code
  driver = webdriver.Chrome()
  driver.get(url = url0)
  elem = driver.find_element_by_name("q")
  elem.send_keys(search1 + " pic " + str(i))
  elem.send_keys(Keys.RETURN)
  data2.write(driver.page_source)
  data2.close()   
  driver.close()  

data3.close()
train0.close()
