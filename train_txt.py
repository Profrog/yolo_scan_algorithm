import os
import shutil
from pathlib import Path



global path
path = "detourl/"

global name_o
name_o = "train.txt"


file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".jpg")]
file_list_py2 = [file for file in file_list if file.endswith(".jpeg")]
file_list_py3 = [file for file in file_list if file.endswith(".png")]

file_a = open(name_o ,"w+")

for test1 in file_list_py:
 file_a.write(path + test1 + "\n")

for test1 in file_list_py2:
 file_a.write(path + test1 + "\n")

for test1 in file_list_py3:
 file_a.write(path + test1 + "\n")
 
file_a.close()
