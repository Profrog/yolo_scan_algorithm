
import datetime
import os
import shutil
import re
from pathlib import Path

#global name_file
#name_file = "coco.names"
#data1 = open(name_file, 'a')

now = datetime.datetime.now()

global path
path = "t_image/"

global path2
path2 = "t_image2/"
 
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".jpg")]
search_num = 0

print ("file_list: {}".format(file_list_py)) 
 
for test1 in file_list_py:
 if True:
  numbers = re.sub(r'[^0-9]', '', test1)
  
  if( int(numbers) % 5 == 0):
   print(path + test1)
   shutil.copy(path + test1, path2 + test1)     
     
     #if label_dir.find(".xml") >= 0:
       #label_dir2 = label_dir.replace(".xml","")
       #data_file = Path(label_dir)
       #data_file.rename(label_dir2)
       #label_dir = label_dir2
              
     #shutil.copy(label_dir, path2)          
     #shutil.copy(label_dir[0:len(label_dir) -4]  + ".jpg", search1)
     #search_num += 1
     #print("find dataset " + str(search_num) + "\n")
     #print(label_dir[0:len(label_dir) -4] + "\n")
         
 #except:   
  #print("error in " + test1 + "\n")  
  #continue


