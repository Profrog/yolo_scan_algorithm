
import os
import shutil


global name_file
name_file = "coco.names"
#data1 = open(name_file, 'a')


global path
path = "image/"


print("모을 label을 입력하시오")
search1 = input()
sequence = -1


i = 0
with open(name_file) as file:
    for line in file.readlines():
     if line == search1 + "\n":
      sequence = i
      break
           
     i += 1
     
     
if sequence == -1:
 print("없는 label입니다")     
 exit()
 
  
if os.path.exists(search1):
 shutil.rmtree(search1) 

os.makedirs(search1)
 
 
print("label index " + str(sequence) + "\n")



file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".txt")]

print ("file_list: {}".format(file_list_py))


search_num = 0

for test1 in file_list_py:
 try:
  with open(path + test1) as file:
   for line in file.readlines():
    label_line = line.split(" ")
    if label_line[0] == str(sequence):
     search_num += 1
     label_dir = path + test1
     
     print("find label " + str(search_num) + "\n")
     shutil.copy(label_dir, search1)
     shutil.copy(label_dir[0:len(label_dir) -4]  + ".jpg", search1)
     #print(label_dir[0:len(label_dir) -4] + "\n")
     break
    
 except:   
  print("error in " + test1 + "\n")  
  continue  
    
   

