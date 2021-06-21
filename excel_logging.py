import pandas as pd
import math

global original_file
original_file = 'direct.xlsx'

global df0_txt
df0_txt = 'config.txt'
global df1_txt
df1_txt = 'direct.txt'
global df2_txt
df2_txt = 'cross_info.txt'
global df3_txt
df3_txt = 'station_info.txt'

global config_x
config_x = 'x offset'

global config_y
config_y = 'y offset'

global make_txt
make_txt = "new_direct.txt"

##########################

global x_offset
global y_offset
global x_offset0
global y_offset0


global cross1
cross1 = []
global station1
station1 = []

global label_cross
label_cross = 0

global label_station
label_station = 0


global sum_d
sum_d = 0

###########################


df0 = pd.read_excel(original_file,sheet_name=0)
df1 = pd.read_excel(original_file,sheet_name=1)
df2 = pd.read_excel(original_file,sheet_name=2)
df3 = pd.read_excel(original_file,sheet_name=3)


df0.to_csv(df0_txt,index= False)
df1.to_csv(df1_txt,index= False)
df2.to_csv(df2_txt,index= False)
df3.to_csv(df3_txt,index= False)

print("xlsx to txt is end")

try:
 with open(df0_txt) as file:
    for line in file.readlines():
      data_list = line.split(',')
    
      if data_list[0] == config_x:
       x_offset = float(data_list[1])
       x_offset0 = x_offset
       print("x_offset " + str(x_offset)) 
     
      elif data_list[0] == config_y: 
       y_offset = float(data_list[1])
       y_offset0 = y_offset
       print("y_offset " + str(y_offset))

except:
 print("error in " + df0_txt) 
 
 
try:
  with open(df2_txt) as file:
    for line in file.readlines():
     try:
      data_list = line.split(',')
      cross1.append([float(data_list[2]),float(data_list[3])])
     except:
      continue
    
    
except:
 print("error in " + df2_txt)
 
  
print("Cross size is " + str(len(cross1)))
 
 
try:
 with open(df3_txt) as file:
    for line in file.readlines():
     try:
      data_list = line.split(',')
      station1.append([float(data_list[3]),float(data_list[4])])
     except:
      continue
    
    
except:
 print("error in " + df3_txt)
 
 
 
print("Station size is " + str(len(station1)))
 
 

m_txt = open(make_txt, 'w+')

try:
 with open(df1_txt) as file: 
    for line in file.readlines():
     try:
      data_list = line.split(',')
      x_op = float(data_list[0])
      y_op = float(data_list[1])
      s_limit = float(data_list[2])      
      sum_d += math.sqrt(math.pow(x_op - x_offset0 , 2) + math.pow(y_op - y_offset0 , 2))  
      x_offset0 = x_op
      y_offset0 = y_op
      
      if label_cross + 1 < len(cross1):
       while math.sqrt(math.pow(x_op - (cross1[label_cross][0] + x_offset) , 2) + math.pow(y_op - (cross1[label_cross][1] + y_offset) , 2)) >= math.sqrt(math.pow(x_op - (cross1[label_cross+1][0] + x_offset) , 2) + math.pow(y_op - (cross1[label_cross+1][1] + y_offset) , 2)):
         label_cross += 1


      if label_cross - 1 >= 0:
       while math.sqrt(math.pow(x_op - (cross1[label_cross][0] + x_offset) , 2) + math.pow(y_op - (cross1[label_cross][1] + y_offset) , 2)) >= math.sqrt(math.pow(x_op - (cross1[label_cross-1][0] + x_offset) , 2) + math.pow(y_op - (cross1[label_cross-1][1] + y_offset) , 2)):
         label_cross -= 1         
                  
      if label_station + 1 < len(station1):
       while math.sqrt(math.pow(x_op - ( station1[label_station][0] + x_offset) , 2) + math.pow(y_op - (station1[label_station][1] + y_offset) , 2)) >= math.sqrt(math.pow(x_op - (station1[label_station+1][0] + x_offset) , 2) + math.pow(y_op - (station1[label_station+1][1] + y_offset), 2)):
         label_station += 1
         
         
      if label_station - 1 >= 0:
       while math.sqrt(math.pow(x_op - ( station1[label_station][0] + x_offset) , 2) + math.pow(y_op - (station1[label_station][1] + y_offset) , 2)) >= math.sqrt(math.pow(x_op - (station1[label_station-1][0] + x_offset) , 2) + math.pow(y_op - (station1[label_station-1][1] + y_offset), 2)):
         label_station -= 1        
         
                    
      data_e = label_cross + 1
      data_f = label_cross + 1
      data_g = label_station + 1
      data_h = label_station + 1
        
      write_m = str(x_op) + "," + str(y_op) + "," + str(s_limit) + "," + str(sum_d) + "," + str(data_e) + "," + str(data_f) + "," + str(data_g) + "," + str(data_h) + "\n"
      m_txt.write(write_m)
      
       
     except:
          
      if len(line) > 0:
       m_txt.write(line)

except:
 print("error in " + df1_txt)



m_txt.close()
df2_2 = pd.read_csv(make_txt,sep=",",encoding='utf-8')
df2_2.to_excel('new_direct.xlsx',index=False)




#txt0 = open(df0_txt, 'a')
#txt1 = open(df1_txt, 'a')
#txt2 = open(df2_txt, 'a')
#txt3 = open(df3_txt, 'a')








































