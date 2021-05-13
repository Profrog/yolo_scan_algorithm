import numpy as np
import matplotlib.pyplot as plt
from bresenham import bresenham

positions = [[0,1] , [0,3] , [3,0] , [1,1], [3,7], [5,8] , [6,9] , [11,11] , [7,11],[13,13],[0,9]]


w = 15
h = 15
yolomap0 = np.zeros((w,h))

dot1 = []
dot2 = []

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
     yolomap0[convex[x1][0],convex[x1][1]] = 3 #data
          
     if x1 < (len(convex) -1):
      x2 = x1 + 1
      dot1.append([convex[x1][0], convex[x1][1]])
      dot2.append([convex[x2][0], convex[x2][1]])
       
          
    for x3 in range(0,len(dot1)):
     print(dot1)    
     bresenham1 = list(bresenham(dot1[x3][0], dot1[x3][1], dot2[x3][0], dot2[x3][1])) 
     for x4 in range(0,len(bresenham1)):
       #print(bresenham1)
       yolomap0[bresenham1[x4][0],bresenham1[x4][1]] = 3 #data
       
    for y0 in range(0,h,1):    
     mode = 0
     last_index = w
             
     for x0 in range(0,w,1):
    
      if mode == 0 and yolomap0[x0,y0] > 1:
       mode = 2
       last_index = x0 + 1

      elif mode == 2 and yolomap0[x0,y0] > 1:
       last_index = x0 + 1


      elif mode == 2 and yolomap0[x0,y0] < 3:       
       yolomap0[x0,y0] = 1
       mode = 3
             
      if mode == 3 and yolomap0[x0,y0] > 1:
       last_index = x0 + 1
      
      elif mode == 3 and yolomap0[x0,y0] < 3:
       yolomap0[x0,y0] = 1

         
     for x1 in range(last_index,w,1):   
      yolomap0[x1,y0] = 0

                 
    return len(convex)
    
    
                
answer = -2
     
positions = sorted(positions, key=lambda pos:(pos[0], pos[1]))
answer += convex_hull(positions)
#bresen_ham()
  
positions.reverse()
answer += convex_hull(positions)
#bresen_ham()
#print(answer)


plt.matshow(yolomap0)
plt.savefig('fig2.png', dpi=300)
plt.show()



