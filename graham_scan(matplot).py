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


print("맵의 사이즈(정사각형)입력, 한 변의 길이값 1개만 입력하세요")
x = int(input())
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
     
    for x3 in range(0,len(convex)):
     test1[convex[x3][0],convex[x3][1]] = 1
     
    
     
     if x3 < (len(convex) -1):
      x4 = x3 + 1
     else:	
      x4 = 0
     
     dot1.append([convex[x3][0], convex[x3][1]])
     dot2.append([convex[x4][0], convex[x4][1]])    
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
#bresen_ham()
  
positions.reverse()
answer += convex_hull(positions)
#bresen_ham()
#print(answer)


plt.matshow(test1)
plt.savefig('fig2.png', dpi=300)
plt.show()

   
       



