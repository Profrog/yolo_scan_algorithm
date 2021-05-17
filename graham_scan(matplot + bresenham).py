import numpy as np
import matplotlib.pyplot as plt
from bresenham import bresenham


global graham_list
graham_list = [[0,1] , [0,3] , [3,0] , [1,1], [3,7], [5,8] , [6,9] , [11,11] , [7,11],[13,13],[0,9]]

map_x = 15
map_y = 15
yolomap0 = np.zeros((map_x,map_y))

dot1 = []
dot2 = []


global outline
outline = 2

global inline
inline = 1


def inclination(p1, p2):
    return p2[0] - p1[0], p2[1] - p1[1]
 
def ccw(p1, p2, p3):
    v, u = inclination(p1, p2), inclination(p2, p3)
    if v[0] * u[1] > v[1] * u[0]:
        return True
    return False
     
def convex_hull():
    global graham_list

    convex = list()
    for p3 in graham_list:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            if ccw(p1, p2, p3):
                break
            convex.pop()
        convex.append(p3)
     
    dot1 = []
    dot2 = []
      
    for x1 in range(0,len(convex)):
     yolomap0[convex[x1][0],convex[x1][1]] = outline #data
          
     if x1 < (len(convex) -1):
      x2 = x1 + 1
      dot1.append([convex[x1][0], convex[x1][1]])
      dot2.append([convex[x2][0], convex[x2][1]])
       
          
    for x3 in range(0,len(dot1)):
     print(dot1)    
     bresenham1 = list(bresenham(dot1[x3][0], dot1[x3][1], dot2[x3][0], dot2[x3][1])) 
     for x4 in range(0,len(bresenham1)):
       yolomap0[bresenham1[x4][0],bresenham1[x4][1]] = outline #data
                      
    return len(convex)
    


def painting():
  global graham_list
  
  for y0 in range(0,map_y,1):    
   mode = 0
   start_index = -1
   end_index = -1
    
   for x0 in range(0,map_x,1):
    
    if mode == 0 and yolomap0[x0,y0] > inline:
     mode = 2
   
    elif mode == 2 and yolomap0[x0,y0] < outline:       
     start_index = x0
     mode = 3
    
    elif mode == 3 and yolomap0[x0,y0] > inline:
     end_index = x0                    
  
  
   if end_index > -1 and start_index > -1:                      
    for x0 in range(start_index,end_index,1):                        
     if yolomap0[x0,y0] < outline:
      yolomap0[x0,y0] = 1



                    
answer = -2

  
graham_list = sorted(graham_list, key=lambda pos:(pos[0], pos[1]))
answer += convex_hull()
#bresen_ham()
  
graham_list.reverse()
answer += convex_hull()
painting()
#bresen_ham()
#print(answer)


plt.matshow(yolomap0)
plt.savefig('fig2.png', dpi=300)
plt.show()


