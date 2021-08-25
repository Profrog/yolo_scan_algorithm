import numpy as np
import matplotlib.pyplot as plt
from bresenham import bresenham
import random
from matplotlib.colors import ListedColormap


positions = []

dot1 = []
dot2 = []

global outline
outline = 2

global inline
inline = 1

global pointline
pointline = 4

global movingline
movingline = 9

global point_list
point_list = []


print("맵의 사이즈(정사각형)입력, 한 변의 길이값 1개만 입력하세요(20보다 큰수)")
global x
x = int(input())
w = x
h = x
test1 = np.zeros((x,x))


global moving
moving = []


answer = -2
cmap = ListedColormap(['w', 'k', 'r','b','g'])

def point_mark(x1,x2,y1,y2,data):    
 for x0 in range(x1,x2 +1,1):
   for y0 in range(y1,y2 +1,1):
     test1[x0,y0] = int(data) #after using other way  



def inclination(p1, p2):
    return p2[0] - p1[0], p2[1] - p1[1]
 
def ccw(p1, p2, p3):
    v, u = inclination(p1, p2), inclination(p2, p3)
    if v[0] * u[1] > v[1] * u[0]:
        return True
    return False
     
def convex_hull(positions):
    global convex
    convex = list()
    for p3 in positions:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            if ccw(p1, p2, p3):
                break
            convex.pop()
        convex.append(p3)
     
    dot1 = []
    dot2 = []
      
    for x1 in range(0,len(convex)):
     test1[convex[x1][0],convex[x1][1]] = 4 #data
          
     if x1 < (len(convex) -1):
      x2 = x1 + 1
      dot1.append([convex[x1][0], convex[x1][1]])
      dot2.append([convex[x2][0], convex[x2][1]])
       
          
    for x3 in range(0,len(dot1)):
     print(dot1)    
     bresenham1 = list(bresenham(dot1[x3][0], dot1[x3][1], dot2[x3][0], dot2[x3][1])) 
     for x4 in range(0,len(bresenham1)):
       if test1[bresenham1[x4][0],bresenham1[x4][1]] < 3:
        test1[bresenham1[x4][0],bresenham1[x4][1]] = 3 #data
                     
    return len(convex)
    
    
    
def painting():
  global position
  global convex
  
  for y0 in range(0,h,1):
      
   global x    
   mode = 0
   start_index = -1
   end_index = -1
    
   for x0 in range(0,w,1):
    
    if mode == 0 and test1[x0,y0] > inline:
     mode = 2
   
    elif mode == 2 and test1[x0,y0] < outline:       
     start_index = x0
     mode = 3
    
    elif mode == 3 and test1[x0,y0] > inline:
     end_index = x0                    
  
  
   if end_index > -1 and start_index > -1:                      
    for x0 in range(start_index,end_index,1):                        
     if test1[x0,y0] < outline:
      test1[x0,y0] = 1    

   
      
def setting_point(n,mode):
 global movingline
 for r0 in range(0,n,1):
  w0 = random.randrange(1,int(x/10))
  h0 = random.randrange(1,int(x/10))
  x00 = random.randrange(w0,int(x - w0))
  y00 = random.randrange(h0,int(x - h0))
  point_mark(x00-w0,x00+w0,y00-h0,y00+h0,mode)
  test1[x00-w0,y00-h0] = pointline
  test1[x00-w0,y00+h0] = pointline
  test1[x00+w0,y00-h0] = pointline
  test1[x00+w0,y00+h0] = pointline
  
  if mode != movingline:
   positions.append([x00-w0,y00-h0])
   positions.append([x00-w0,y00+h0])
   positions.append([x00+w0,y00-h0])
   positions.append([x00+w0,y00+h0])
   
def setting_point2(mode):
 global movingline
 for line in point_list:
  data = line.split(',')
  x00 = int(data[0])
  y00 = int(data[1])
  w0 = int(data[2])
  h0 = int(data[3])
    
  point_mark(x00,x00+w0,y00,y00+h0,mode)
  test1[x00,y00] = pointline
  test1[x00,y00+h0] = pointline
  test1[x00+w0,y00] = pointline
  test1[x00+w0,y00+h0] = pointline
  
  if mode != movingline:
   positions.append([x00,y00])
   positions.append([x00,y00+h0])
   positions.append([x00+w0,y00])
   positions.append([x00+w0,y00+h0])   
   
 


while True:
 if True:
  answer = -2
  print("-1을 누르면 종료, 0은 get.txt에서 데이터 값 가져와서 실행[x,y,w,h], 나머지 수는 자동모드")
  checking = int(input())
 
  if checking == -1:
   break

  elif checking == 0: #x,y,w,h
   with open("get.txt", "r") as f:
    point_list = [line.strip() for line in f.readlines()]
    
   setting_point2(outline)
       
  else:
   print("입력받을 개체 수를 입력하세요")
   n = int(input()) 
   setting_point(n,outline)
  
  
  
  plt.matshow(test1,cmap=cmap)
  plt.grid(True, color = 'black')
 
 
  plt.savefig('fig1.png', dpi=300)
   
  positions = sorted(positions, key=lambda pos:(pos[0], pos[1]))
  answer += convex_hull(positions)
  positions.reverse()
  answer += convex_hull(positions)
  plt.matshow(test1,cmap=cmap)
  plt.grid(True, color = 'black')
  
  plt.savefig('fig2.png', dpi=300)
  
  painting()
  plt.matshow(test1,cmap=cmap)
  plt.grid(True, color = 'black')
  plt.savefig('fig3.png', dpi=300)
   #plt.show()
     
 #except:
  #print("ERROR")



#개체는 직사각형
#matplot 3은 개체의 내부
#        1은 개체 사이의 영역   
#        0은 빈 공간       
#        7은 개체의 꼭짓점(convex_hull input)
#        8은 convex_hull output

