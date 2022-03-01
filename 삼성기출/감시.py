from copy import deepcopy

N,M = map(int, input().split())

graph = [[0 for _ in range(M)] for _ in range(N)]
cctvXY = []

for row in range(N):  
  items = list(map(int,input().split()))
  for col in range(len(items)):
    graph[row][col] = items[col]
    if 0 < items[col] and items[col] < 6:
      cctvXY.append((row,col))

# 0 왼쪽, 1 오른쪽, 2 위쪽, 3 아래쪽
cctv = []
cctv.append([[0],[1],[2],[3]])
cctv.append([[0,1],[2,3]])
cctv.append([[0,3],[0,2],[2,1],[1,3]])
cctv.append([[0,1,2],[0,1,3],[0,3,2],[1,3,2]])
cctv.append([[0,1,2,3]])

posx = [0,0,-1,1]
posy = [-1,1,0,0]

result = 99999
def dfs(board, tvIdx):
  global result

  if tvIdx == len(cctvXY):
    answer = 0
    for i in range(N):
      for j in range(M):
        if board[i][j] == 0:
          answer += 1

    result = min(result, answer)
  
  else:
    cc = cctvXY[tvIdx]        
    x = cc[0]
    y = cc[1]
      
    ccvalue = graph[x][y]
      
    for i in cctv[ccvalue-1]:
      myboard = deepcopy(board)      
      
      for j in i:
        ex = 0
        ey = 0
        while True:
          ex += posx[j]
          ey += posy[j]
          
          dx = x + ex
          dy = y + ey   
            
          if 0 <= dx and dx < N and dy < M and 0 <= dy:
            if myboard[dx][dy] == 6:
              break
            elif 0 < myboard[dx][dy] and  myboard[dx][dy] < 6:
              continue
            else: 
              myboard[dx][dy] = 7
          else:
            break
                
      dfs(myboard, tvIdx+1)
    
dfs(graph, 0)

print(result)
  