from collections import deque

<<<<<<< HEAD
N = int(input())
# 아기상어 좌표 뚜루루뚜루
sharkx, sharky = -1, -1
sharkSize = 2

board = [[0 for _ in range(N)]for _ in range(N)]

for i in range(N):
  fished = list(map(int,input().split()))    
  for j in range(N):
    if fished[j] == 9:
      sharkx, sharky = i,j
      board[i][j] = 0
    elif 7 > fished[j] > 0:
      board[i][j] = fished[j]

pos = [(1,0),(0,1),(-1,0),(0,-1)]
      
# 좌표, 사이즈
def active(x,y,sz):  
  # 방문처리
  visited = [[False for _ in range(N)]for _ in range(N)]
  visited[x][y] = True

  # 먹은거
  eat = []
  
  queue = deque()
  queue.append((x,y,0))
  # 현재 최소 거리
  minRange = 10000000
  
  while queue:
    x,y,z = queue.popleft()

    if 0 < board[x][y] < sz and z <= minRange:            
        # 먹은거로 처리
        eat.append((x,y,z))       
        minRange = z

    for i in range(4):
      dx = x + pos[i][0]
      dy = y + pos[i][1]
      
      if 0 <= dx < N and 0 <= dy < N and visited[dx][dy] == False:        
        if board[dx][dy] <= sz:
          queue.append((dx,dy,z+1))
          visited[dx][dy] = True
              
  if len(eat) > 0 :
    eat.sort(key = lambda x: (x[0],x[1]))
    # 리턴 값 고기 없앰
    ex = eat[0][0]
    ey = eat[0][1]
    board[ex][ey] = 0    

    return eat[0]
  else:
    return -1

answer = 0
eatCnt = 0
while True:    
  value = active(sharkx,sharky,sharkSize)
  # -1 이면 더이상 먹을 물고기가 없음
  if value == -1:
      break

  sharkx = value[0]
  sharky = value[1]
  answer += value[2]
  eatCnt += 1

  if eatCnt == sharkSize:
    sharkSize += 1
    eatCnt = 0

print(answer)
  
