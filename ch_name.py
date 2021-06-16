
import os
import shutil
from pathlib import Path

#global name_file
#name_file = "coco.names"
#data1 = open(name_file, 'a')


global path
path = "laneclosed1/"

global search1
search1 = "a"

file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".txt")]
search_num = 0

print ("file_list: {}".format(file_list_py)) 
 
for test1 in file_list_py:
 try:
  with open(path + test1) as file:
     label_dir = path + test1 
     label_dir2 = label_dir.replace(".txt", search1 + ".txt")
     data_file = Path(label_dir)
     data_file.rename(label_dir2)
     label_dir = label_dir2
  
         
 except:   
  print("error in " + test1 + "\n")  
  continue


file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".jpg")]
search_num = 0

print ("file_list: {}".format(file_list_py)) 
 
for test1 in file_list_py:
 try:
  with open(path + test1) as file:
     label_dir = path + test1 
     label_dir2 = label_dir.replace(".jpg",search1 + ".jpg")
     data_file = Path(label_dir)
     data_file.rename(label_dir2)
     label_dir = label_dir2
  
         
 except:   
  print("error in " + test1 + "\n")  
  continue





  
  
    
