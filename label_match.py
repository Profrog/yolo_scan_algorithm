import datetime
import os
import shutil
from pathlib import Path

#global name_file
#name_file = "coco.names"
#data1 = open(name_file, 'a')

now = datetime.datetime.now()

global path
path = "t_image/"

global search1
search1 = "endroad" + "_" +  str(now.strftime("%m")) + str(now.strftime("%d"))


if os.path.exists(search1):
 print("already has file") 

else:
 os.makedirs(search1)
 
 
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".txt")]
search_num = 0

print ("file_list: {}".format(file_list_py)) 
 
for test1 in file_list_py:
 try:
  with open(path + test1) as file:
     label_dir = path + test1
     
     
     if label_dir.find(".xml") >= 0:
       label_dir2 = label_dir.replace(".xml","")
       data_file = Path(label_dir)
       data_file.rename(label_dir2)
       label_dir = label_dir2
              
     shutil.copy(label_dir, search1)          
     shutil.copy(label_dir[0:len(label_dir) -4]  + ".jpg", search1)
     search_num += 1
     print("find dataset " + str(search_num) + "\n")
     #print(label_dir[0:len(label_dir) -4] + "\n")
         
 except:   
  print("error in " + test1 + "\n")  
  continue


write_data = search1 + ".txt"  
filea = open(write_data, 'w+')
file_list2 = os.listdir(search1 + "/")  
file_list_py2 = [file for file in file_list2 if file.endswith(".txt")]  
print("all data_num is " + str(len(file_list_py2)) + "\n")   
filea.write("all data_num is " + str(len(file_list_py2)) + "\n")  
  
  
  
  
  
  
    
