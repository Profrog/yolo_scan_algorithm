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


def fetch_image_urls(query:str, max_links_to_fetch:int, wd:webdriver, sleep_between_interactions:int=1):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)    
    
    # build the google query
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

    # load the page
    wd.get(search_url.format(q=query))

    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
        scroll_to_end(wd)

        # get all image thumbnail results
        thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
        number_results = len(thumbnail_results)
        
        print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")
        
        for img in thumbnail_results[results_start:number_results]:
            # try to click every thumbnail such that we can get the real image behind it
            try:
                img.click()
                time.sleep(sleep_between_interactions)
            except Exception:
                continue

            # extract image urls    
            actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))
                    data3.write(str(actual_image.get_attribute('src')) + "\n")

            image_count = len(image_urls)

            if len(image_urls) >= max_links_to_fetch:
                print(f"Found: {len(image_urls)} image links, done!")
                break
        else:
            print("Found:", len(image_urls), "image links, looking for more ...")
            time.sleep(30)
            return
            load_more_button = wd.find_element_by_css_selector(".mye4qd")
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")

        # move the result startpoint further down
        results_start = len(thumbnail_results)
    
    wd.close()
    return image_urls
    
    
print("검색할 커맨드를 입력하시오")
search1 = input()    
    
print("몇 개를 검색하시겠습니까")
n = int(input())   


driver = webdriver.Chrome()    
fetch_image_urls(search1, n, driver, 1)
data3.close()
 

    
i = 1

while i <= n:
 with open('crol.txt') as file:
  for line in file.readlines():
   try:    
    urllib.request.urlretrieve(line, file_name + "/" + image_name + str(i) + '.jpg')
    i+=1
    
    if i > n:
     break
    
   except: 
    print("Error is" + line + "\n")
  
  if i <= n: 
   fetch_image_urls(search1 + " pic " + str(i), n-i, driver, 1)   
    
    
