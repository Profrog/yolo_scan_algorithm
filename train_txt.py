import os
import shutil
from pathlib import Path



global path
path = "t_image/"


file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".jpg")]
file_a = open("train_a.txt" ,"w+")

for test1 in file_list_py:
 file_a.write(path + test1 + "\n")
 
