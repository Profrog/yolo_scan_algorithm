from PIL import Image
import os
import time
import urllib.request
import ssl

global n
n = 100


f = open("crol_box.txt", 'r',encoding='UTF-8')
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
    
     data3.write(str1 + '\n')
     urllib.request.urlretrieve(str1, 't_image/test' + str(i) + '.jpg')
     i+=1
    
    if not line: break
    
  except:
     print("error " + str1)
     i -= 1
   
f.close()
