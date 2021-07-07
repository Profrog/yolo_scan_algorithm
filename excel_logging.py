###################라이브러리
import pandas as pd
import math
##########################
global original_file
original_file = 'direct.xlsx'  #읽을 excel 파일 원본

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

global out_txt
out_txt = "new_direct.txt"  #경로 갱신 데이터

global out_xlsx
out_xlsx = 'new_direct.xlsx' #최종 저장 파일

global x_offset
global y_offset
global x_offset0
global y_offset0

global cross1 #교차로의 좌표가 저장될 리스트
cross1 = []
global station1 #정거장의 좌표가 저장될 리스트
station1 = []

global label_cross #교차로 인덱스
label_cross = 0

global label_station #정거장 인덱스
label_station = 0

global sum_d #누적이동거리
sum_d = 0

global change_point #교차로(정거장) 현재 좌표 간 오차 인정 범위
change_point = 15

###########################


def dia(a_x, b_x, a_y,b_y): ##a,b 사이의 거리
 return math.sqrt(math.pow(a_x - b_x , 2) + math.pow(a_y - b_y , 2))

def sca_p(a_x, b_x,a_y,b_y): 
 if a_x * b_x >= 0 and a_y * b_y >= 0:
  return True

 else:
  return False
  
def sca_p2(a_x, b_x,a_y,b_y): ##a,b 사이의 내적
 if a_x * b_x + a_y * b_y >= 0:
  return True

 else:
  return False  

df0 = pd.read_excel(original_file,sheet_name=0)#config 시트
df1 = pd.read_excel(original_file,sheet_name=1)#경로 시트
df2_0 = pd.read_excel(original_file,sheet_name=2)#교차로정보 시트
df2 = pd.read_excel(original_file,sheet_name=3)#교차로 시트
df3 = pd.read_excel(original_file,sheet_name=4)#정거장정보 시트

df0.to_csv(df0_txt,index= False)#config -> config.txt
df1.to_csv(df1_txt,index= False)#경로 -> direct.txt
df2.to_csv(df2_txt,index= False)#교차로 -> cross_info.txt
df3.to_csv(df3_txt,index= False)#정거장정보 -> station_info.txt

print("xlsx to txt is end")

try: #config-> x,y offset 얻기
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
 
 
try: #교차로 -> 교자로 좌표 리스트
  with open(df2_txt) as file:
    for line in file.readlines():
     try:
      data_list = line.split(',')
      cross1.append([float(data_list[2]) + x_offset,float(data_list[3]) + y_offset, int(data_list[1])])
     except:
      continue
       
except:
 print("error in " + df2_txt)
 
  
print("Cross size is " + str(len(cross1)))
 
 
try: #정거장 정보 -> 정거장 좌표 리스트
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

 

m_txt = open(out_txt, 'w+')

try:
 with open(df1_txt) as file: #경로 정보 읽기 
    for line in file.readlines():
     try:
      data_list = line.split(',') #현 좌표 얻기
      x_op = float(data_list[0])
      y_op = float(data_list[1])
      s_limit = float(data_list[2]) 
      
      if x_offset0 == 0:
       x_offset0 = x_op
       
       while dia(x_op,cross1[label_cross+1][0],y_op,cross1[label_cross+1][1]) < dia(x_op,cross1[label_cross][0],y_op,cross1[label_cross][1]): 
        label_cross += 1 #첫 좌표일시 가장 가까운 교차로 정보 획득
       
       while dia(x_op,station1[label_station+1][0],y_op,station1[label_station+1][1]) < dia(x_op,station1[label_station][0],y_op,station1[label_station][1]): 
        label_station += 1 #첫 좌표일시 가장 가까운 정거장 정보 획득
            
      
      if y_offset0 == 0:
       y_offset0 = y_op
                 
      sum_d += math.sqrt(math.pow(x_op - x_offset0 , 2) + math.pow(y_op - y_offset0 , 2))#시작한 지점부터 이동거리 누적
      
      x_vector = x_op - x_offset0
      y_vector = y_op - y_offset0  
        
      x_offset0 = x_op
      y_offset0 = y_op
      
      label_cross_0 = label_cross
      label_station_0 = label_station
      
                 
      if label_cross + 1 < len(cross1): 
       if dia(x_op,cross1[label_cross][0],y_op,cross1[label_cross][1]) < change_point: #(현재 좌표-교차로)일정 거리 보다 가까워질 경우 도착한 것으로 인식 다음 교차로로 정보 갱신
        label_cross += 1  
                                      
      if label_station + 1 < len(station1) : 
        if dia(x_op,station1[label_station][0],y_op,station1[label_station][1]) < change_point: #(현재 좌표-정거장)일정 거리 보다 가까워질 경우 도착한 것으로 인식 다음 정거장으로 정보 갱신
         label_station += 1  
                                    
      data_e = label_station + 1
      data_f = label_cross + 1
      data_g = cross1[label_cross+1][2]
      #data_h = label_station
      
      cross_x = ""
      cross_y = ""
      station_x = ""
      station_y = ""
      
      
      if label_cross_0 != label_cross: #교차로 인덱스가 바뀐 경우 xlsx에 표기
       cross_x = str(cross1[label_cross][0])
       cross_y = str(cross1[label_cross][1])
      
      if label_station_0 != label_station: #정거장 인덱스가 바뀐 경우 xlsx에 표기
       station_x = str(station1[label_station_0][0])
       station_y = str(station1[label_station_0][1])
           
      write_m = str(x_op) + "," + str(y_op) + "," + str(s_limit) + "," + str(sum_d) + "," + str(data_e) + "," + str(data_f) + "," + str(data_g) + "," + str(cross_x) + "," + str(cross_y) + "," + str(station_x) + "," + str(station_y) + "\n"
      m_txt.write(write_m)
            
     except:         
      if len(line) > 0:
       m_txt.write(str(line[0:len(line) - 1]) + str("," + "cross_x" + "," + "cross_y" + "," + "station_x" + "," + "station_y" + "\n"))

except:
 print("error in " + df1_txt)

m_txt.close()
df1_2 = pd.read_csv(out_txt,sep=",",encoding='utf-8', low_memory=False)

with pd.ExcelWriter(out_xlsx,index=False) as writer: #df 파일들 excel로 변환
 df0.to_excel(writer,sheet_name = 'config',index=False)
 df1_2.to_excel(writer,sheet_name = '경로',index=False)
 df2_0.to_excel(writer,sheet_name = '교차로정보',index=False)
 df2.to_excel(writer,sheet_name = '교차로',index=False)
 df3.to_excel(writer,sheet_name = '정거장정보',index=False)
 






