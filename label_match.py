
import os
import shutil


#global name_file
#name_file = "coco.names"
#data1 = open(name_file, 'a')


global path
path = "t_image/"

global search1
search1 = "working1"


if os.path.exists(search1):
 shutil.rmtree(search1) 

os.makedirs(search1)
 
 
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".txt")]

print ("file_list: {}".format(file_list_py)) 
 
for test1 in file_list_py:
 try:
  with open(path + test1) as file:
     label_dir = path + test1     
     shutil.copy(label_dir, search1)
     shutil.copy(label_dir[0:len(label_dir) -8]  + ".jpg", search1)
     #print(label_dir[0:len(label_dir) -4] + "\n")
         
 except:   
  print("error in " + test1 + "\n")  
  continue  
