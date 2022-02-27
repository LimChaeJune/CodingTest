import copy
from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

N,M = map(int, input().split())

graph = [[0 for _ in range(M)] for _ in range(N)]
virus = []
safe = []

for i in range(N):
  values = list(map(int, input().split()))
  for j in range(len(values)):
    if values[j] == 2:
      virus.append((i,j))
    elif values[j] == 0:
      safe.append((i,j))
    graph[i][j] =  values[j]


posx = [0,0,1,-1]
posy = [1,-1,0,0]
def bfs(copyGraph):        
  queue = deque()    
  
  for i in virus:
    queue.append((i[0],i[1]))

  while(queue):
    x, y = queue.popleft()        
    
    for i in range(4):
      dx = x + posx[i]
      dy = y + posy[i]
      
      if dx < 0 or dx >= N or dy < 0 or dy >= M or copyGraph[dx][dy] == 2:
          continue
      
      if copyGraph[dx][dy] == 0:  
          copyGraph[dx][dy] = 2
          queue.append((dx,dy))              
        

  
result = 0
combis = []

for i in combinations(safe,3):
    combis.append(i)

for comb in combis:            
  copyGp = copy.deepcopy(graph)

  for com in comb:
    copyGp[com[0]][com[1]] = 1
  
 

  bfs(copyGp)
  
  newresult = 0
  for i in range(N):
      for j in range(M):
          if copyGp[i][j] == 0:
            newresult += 1

  result = max(result, newresult)

          

print(result)
  
    