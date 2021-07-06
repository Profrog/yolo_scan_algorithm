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

data3 = open('crol.txt', 'w+')
global file_name
file_name = 't_image'

global image_name
image_name = "endroad" + str(datetime.datetime.now().date())

if os.path.exists(file_name):
 shutil.rmtree(file_name) 

os.makedirs(file_name)



print("검색할 커맨드를 입력하시오")
search1 = input()    
    
print("몇 개를 검색하시겠습니까")
n = int(input())   

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl") #구글에 이미지탭 URL 주소
elem = driver.find_element_by_name("q")#검색창 태그찾기
elem.send_keys(search1)#찾은 검색창에 찾고 싶은 키워드 입력
elem.send_keys(Keys.RETURN)#입력받은 키를 누른다
SCROLL_PAUSE_TIME = 1


last_height = driver.execute_script("return document.body.scrollHeight")#스크롤 높이 가져옴
count = 1
while count < n:

# 끝까지 스크롤 다운
 driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# 1초 대기를 해야 막힘없이 동작한다.
 time.sleep(SCROLL_PAUSE_TIME)

# 스크롤 다운 후 스크롤 높이 다시 가져옴
 new_height = driver.execute_script("return document.body.scrollHeight")
 if new_height == last_height:
    try:
        driver.find_element_by_css_Selector(".mye4qd").click #첫번째 큰 이미지를 클릭한다.
    except:
        break
 last_height = new_height
 images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd") #이미지를 눌렀을때 나오는 큰 이미지의 태그를 찾는다.
 
 for image in images:
    try:
        if count > n:
         break
        print(count)
        count = count + 1
        image.click()
        #time.sleep(2)
        imgURL = image.get_attribute("src")# 찾은 이미지의 FullxPath를 복사 붙여넣어서 다운로드              
        #print(imgURL)
        urllib.request.urlretrieve(imgURL, file_name + "/" + image_name + str(count))
        os.rename(file_name + "/" + image_name + str(count), file_name + "/" + image_name + str(count) + "." + str(imghdr.what(file_name + "/" + image_name + str(count))))
        
        
        
    except:
        print("error")
        
        
        
               
#driver.close()        
        
        
        
        
        
        
        
        

driver.close()
