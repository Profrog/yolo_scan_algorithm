import numpy as np
import matplotlib.pyplot as plt
from bresenham import bresenham

positions = [[0,1] , [0,3] , [3,0] , [1,1], [3,7], [5,8] , [6,9] , [11,11]]
test1 = np.zeros((1000,1000))

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
     
    for x3 in range(0,len(convex)):
     test1[convex[x3][0],convex[x3][1]] = 1
     
    
     
     if x3 < (len(convex) -1):
      x4 = x3 + 1
     else:	
      x4 = 0
     
     dot1.append([convex[x3][0], convex[x3][1]])
     dot2.append([convex[x4][0], convex[x4][1]])    
    return len(convex)
    

   
       
#n, answer = int(input()), -2
answer = -2
#positions = list()
#for i in range(n):
    #positions.append(list(map(int, input().split())))
     
positions = sorted(positions, key=lambda pos:(pos[0], pos[1]))
answer += convex_hull(positions)
#bresen_ham()
  
positions.reverse()
answer += convex_hull(positions)
#bresen_ham()
#print(answer)


plt.matshow(test1)
plt.savefig('fig2.png', dpi=300)
plt.show()


