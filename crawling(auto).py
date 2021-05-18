from PIL import Image
import os
import time
import urllib.request
import urllib

import time
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait




global n
n = 10

global url0
url0 = "https://www.google.co.kr/imghp?hl=ko&ogbl"



print("검색할 커맨드를 입력하시오")
search1 = input()

data2 = open('crol_box.txt' , 'a')
driver = webdriver.Chrome()
driver.get(url = url0)
elem = driver.find_element_by_name("q")
elem.send_keys(search1)
elem.send_keys(Keys.RETURN)

data2.write(driver.page_source)
data2.close()


print("몇 개를 검색하시겠습니까")
n = int(input())

f = open("crol_box.txt", 'r', encoding='UTF-8')
data3 = open('crol.txt', 'a')
i = 0
while i <= n:
  try:
    line = f.readline()
    
    if line.find(".jpg")== -1:
     continue
    else:
     
     a = line.find(".jpg") + 5
     b = line.find("h")
     str0 = line[b-1:a]
     str1 = str0[1:len(str0) -1]
     #print(str1)
    
     data3.write(str1 + "\n")
     urllib.request.urlretrieve(str1, 't_image/test' + str(i) + '.jpg')
     i+=1
    
    if not line: break
    
  except:
     print("error " + str1)
     i-=1
   
f.close()
data3.close()

