import numpy as np
import matplotlib.pyplot as plt
from bresenham import bresenham
import random

positions = []

dot1 = []
dot2 = []

print("입력받을 개채 수를 입력하세요")
n = int(input())
answer = -2


print("맵의 사이즈(정사각형)입력, 한 변의 길이값 1개만 입력하세요(20보다 큰수)")
x = int(input())
w = x
h = x
test1 = np.zeros((x,x))

#n, answer = int(input()), -2
answer = -2
#positions = list()
#for i in range(n):
    #positions.append(list(map(int, input().split())))
     
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
     test1[convex[x1][0],convex[x1][1]] = 3 #data
          
     if x1 < (len(convex) -1):
      x2 = x1 + 1
      dot1.append([convex[x1][0], convex[x1][1]])
      dot2.append([convex[x2][0], convex[x2][1]])
       
          
    for x3 in range(0,len(dot1)):
     print(dot1)    
     bresenham1 = list(bresenham(dot1[x3][0], dot1[x3][1], dot2[x3][0], dot2[x3][1])) 
     for x4 in range(0,len(bresenham1)):
       #print(bresenham1)
       test1[bresenham1[x4][0],bresenham1[x4][1]] = 3 #data
       
    for y0 in range(0,h,1):    
     mode = 0
     last_index = w
             
     for x0 in range(0,w,1):
    
      if mode == 0 and test1[x0,y0] > 1:
       mode = 2
       last_index = x0 + 1

      elif mode == 2 and test1[x0,y0] > 1:
       last_index = x0 + 1


      elif mode == 2 and test1[x0,y0] < 3:       
       test1[x0,y0] = 1
       mode = 3
             
      if mode == 3 and test1[x0,y0] > 1:
       last_index = x0 + 1
      
      elif mode == 3 and test1[x0,y0] < 3:
       test1[x0,y0] = 1

         
     for x1 in range(last_index,w,1):   
      test1[x1,y0] = 0



     for x1 in range(0,len(convex)):
      test1[convex[x1][0],convex[x1][1]] = 8 #data
                 
    return len(convex)
    


for r0 in range(0,n,1):
 w0 = random.randrange(1,int(x/10))
 h0 = random.randrange(1,int(x/10))
 x00 = random.randrange(w0,int(x - w0))
 y00 = random.randrange(h0,int(x - h0))
 point_mark(x00-w0,x00+w0,y00-h0,y00+h0,3)
 test1[x00-w0,y00-h0] = 2
 test1[x00-w0,y00+h0] = 2
 test1[x00+w0,y00-h0] = 2
 test1[x00+w0,y00+h0] = 2
 positions.append([x00-w0,y00-h0])
 positions.append([x00-w0,y00+h0])
 positions.append([x00+w0,y00-h0])
 positions.append([x00+w0,y00+h0])
 
 
    
positions = sorted(positions, key=lambda pos:(pos[0], pos[1]))
answer += convex_hull(positions)
for r2 in range(0,len(positions),1):
 if test1[positions[r2][0],positions[r2][1]] < 7:
  test1[positions[r2][0],positions[r2][1]] = 7

#bresen_ham()
  
positions.reverse()
answer += convex_hull(positions)
for r2 in range(0,len(positions),1):
 if test1[positions[r2][0],positions[r2][1]] < 7:
  test1[positions[r2][0],positions[r2][1]] = 7
#bresen_ham()
#print(answer)


plt.matshow(test1)
plt.savefig('fig2.png', dpi=300)
plt.show()

#개체는 직사각형
#matplot 3은 개체의 내부
#        1은 개체 사이의 영역   
#        0은 빈 공간       
#        7은 개체의 꼭짓점(convex_hull input)
#        8은 convex_hull output


