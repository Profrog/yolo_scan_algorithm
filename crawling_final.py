from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import imghdr
from PIL import Image
import os
import time
import urllib.request
import urllib
import socket
import shutil
from os import system,chdir
import datetime

import time
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui, sys

data3 = open('crol.txt', 'w+')
global file_name
file_name = 't_image'

global image_name
image_name = "detourr" + str(datetime.datetime.now().date())

if os.path.exists(file_name):
 shutil.rmtree(file_name) 

os.makedirs(file_name)

global driver
driver = webdriver.Chrome()

global SCROLL_PAUSE_TIME
SCROLL_PAUSE_TIME = 1

global last_height
last_height = driver.execute_script("return document.body.scrollHeight")

def keyboard1(str_a):
 #pyautogui.press('c')
 a0 = list(str_a)
 for i in a0:
  pyautogui.press(i)
  time.sleep(0.01)
  
def crol_a(search_1):
 driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl") #구글에 이미지탭 URL 주소
 elem = driver.find_element_by_name("q")#검색창 태그찾기
 elem.send_keys(search_1)#찾은 검색창에 찾고 싶은 키워드 입력
 elem.send_keys(Keys.RETURN)#입력받은 키를 누른다
 global last_height
 last_height = driver.execute_script("return document.body.scrollHeight")#스크롤 높이 가져옴
 
print("검색할 커맨드를 입력하시오")
search1 = input()    
    
print("몇 개를 검색하시겠습니까")
n = int(input())   


crol_a(search1)
count = 1
while count < n:
 try:

  # 끝까지 스크롤 다운
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  # 1초 대기를 해야 막힘없이 동작한다.
  time.sleep(SCROLL_PAUSE_TIME)

  # 스크롤 다운 후 스크롤 높이 다시 가져옴
  new_height = driver.execute_script("return document.body.scrollHeight")
  if new_height == last_height:
    try:
        driver.find_element_by_css_Selector(".mye4qd") #첫번째 큰 이미지를 클릭한다.
            
        
    except:
        break
  last_height = new_height
  images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd") #이미지를 눌렀을때 나오는 큰 이미지의 태그를 찾는다.
  #driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

 
  for image in images:   
        if count > n:
         break
        print(count)
        
        image.click()
        
        x = 680
        y = 340
        
        pyautogui.moveTo(x, y)
        time.sleep(0.1)
        pyautogui.click(button='right')
        time.sleep(0.1)
        pyautogui.moveTo(x + 15, y + 215)
        time.sleep(0.1)
        pyautogui.click(button='left')
        time.sleep(0.1)
        keyboard1(search1 + str(count))
        
        #pyautogui.moveTo(906, 675)
        #pyautogui.click(button='left')
        
        time.sleep(0.1)
        pyautogui.moveTo(1205, 1075) 
        pyautogui.click(button='left')       
        time.sleep(1)
        imgURL = image.get_attribute("src")# 찾은 이미지의 FullxPath를 복사 붙여넣어서 다운로드              
        #print(imgURL)
        urllib.request.urlretrieve(imgURL, file_name + "/" + image_name + str(count))
        os.rename(file_name + "/" + image_name + str(count), file_name + "/" + image_name + str(count) + "." + str(imghdr.what(file_name + "/" + image_name + str(count))))
        count = count + 1
        
        
 except:
  print("error")
  crol_a(search1 + str(count))
  #driver.close()
        
#chdir('labelImg')
#os.system('python3 labelImg.py')                       
#driver.close()        
        
        
       
driver.close()

