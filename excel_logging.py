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

global count_station
count_station = False


global sum_d
sum_d = 0

###########################


def dia(a_x, b_x, a_y,b_y):
 return math.sqrt(math.pow(a_x - b_x , 2) + math.pow(a_y - b_y , 2))

def sca_p(a_x, b_x,a_y,b_y):
 if a_x * b_x >= 0 and a_y * b_y >= 0:
  return True

 else:
  return False
  
def sca_p2(a_x, b_x,a_y,b_y):
 if a_x * b_x + a_y * b_y >= 0:
  return True

 else:
  return False  


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
       x_offset0 = 0
       print("x_offset " + str(x_offset)) 
     
      elif data_list[0] == config_y: 
       y_offset = float(data_list[1])
       y_offset0 = 0
       print("y_offset " + str(y_offset))

except:
 print("error in " + df0_txt) 
 
 
try:
  with open(df2_txt) as file:
    for line in file.readlines():
     try:
      data_list = line.split(',')
      cross1.append([float(data_list[2]) + x_offset,float(data_list[3]) + y_offset])
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
      station1.append([float(data_list[3]) + x_offset,float(data_list[4]) + y_offset])
     except:
      continue
    
    
except:
 print("error in " + df3_txt)
  
print("Station size is " + str(len(station1)))

 

m_txt = open(make_txt, 'w+')
m_txt2 = open("test_module.txt", 'w+')

try:
 with open(df1_txt) as file: 
    for line in file.readlines():
     try:
      data_list = line.split(',')
      x_op = float(data_list[0])
      y_op = float(data_list[1])
      s_limit = float(data_list[2]) 
      
      if x_offset0 == 0:
       x_offset0 = x_op
      
      if y_offset0 == 0:
       y_offset0 = y_op
                 
      sum_d += math.sqrt(math.pow(x_op - x_offset0 , 2) + math.pow(y_op - y_offset0 , 2))
      
      x_vector = x_op - x_offset0
      y_vector = y_op - y_offset0  
        
      x_offset0 = x_op
      y_offset0 = y_op
      
      label_cross_0 = label_cross
      label_station_0 = label_station
      
      #m_txt2.write(str(x_vector) + " " + str(y_vector)+ "\n") 
            
      if label_cross + 1 < len(cross1): 
       while dia(x_op,cross1[label_cross+1][0],y_op,cross1[label_cross+1][1]) < dia(x_op,cross1[label_cross][0],y_op,cross1[label_cross][1]): 
        label_cross += 1
        
        if sca_p2(x_op - (cross1[label_cross][0]),(cross1[label_cross + 1][0] - cross1[label_cross][0]),(y_op - (cross1[label_cross][1])),((cross1[label_cross + 1][1]) - cross1[label_cross][1])):
         label_cross += 1     
       
                 
      if label_station + 1 < len(station1) : 
       while dia(x_op,station1[label_station+1][0],y_op,station1[label_station+1][1]) < dia(x_op,station1[label_station][0],y_op,station1[label_station][1]): 
        label_station += 1
               
       if sca_p2(x_op - (station1[label_station][0]),(station1[label_station + 1][0] - station1[label_station][0]),(y_op - (station1[label_station][1])),((station1[label_station + 1][1]) - station1[label_station][1])):
        label_station += 1     
       
                      
      data_e = label_cross
      data_f = label_cross
      data_g = label_station
      data_h = label_station
      
      cross_x = ""
      cross_y = ""
      station_x = ""
      station_y = ""
      
      
      if label_cross_0 != label_cross:
       cross_x = str(cross1[label_cross][0])
       cross_y = str(cross1[label_cross][1])
      
      if label_station_0 != label_station:
       station_x = str(station1[label_station_0][0])
       station_y = str(station1[label_station_0][1])
      
          
      write_m = str(x_op) + "," + str(y_op) + "," + str(s_limit) + "," + str(sum_d) + "," + str(data_e) + "," + str(data_f) + "," + str(data_g) + "," + str(data_h) + "," + str(cross_x) + "," + str(cross_y) + "," + str(station_x) + "," + str(station_y) + "\n"
      m_txt.write(write_m)
      m_txt2.write(str(data_g)+ "\n") 
      
       
     except:         
      if len(line) > 0:
       m_txt.write(str(line[0:len(line) - 1]) + str("," + "cross_x" + "," + "cross_y" + "," + "station_x" + "," + "station_y" + "\n"))

except:
 print("error in " + df1_txt)



m_txt.close()
df2_2 = pd.read_csv(make_txt,sep=",",encoding='utf-8', low_memory=False)
df2_2.to_excel('new_direct.xlsx',index=False)


m_txt2.close()




#txt0 = open(df0_txt, 'a')
#txt1 = open(df1_txt, 'a')
#txt2 = open(df2_txt, 'a')
#txt3 = open(df3_txt, 'a')






