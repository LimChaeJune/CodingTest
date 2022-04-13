from collections import deque

N =  input()
shark = 2
sharkX = -1
sharkY = -1
board = []
fishes = [0] * (N + 1)
pos = [(0,1),(1,0),(0,-1),(-1,0)]

for i in range(N):
  values = list(map(int,input().split()))
  board.append(values)
  for j in range(values):
    if values[j] == 9:
      sharkX, sharkY = i, j      
    if 7 > values[j] > 0:
      fishes[j] += 1

if fishes[1] == 0:
  print(0)
  exit()

def bfs():
  visited = [[[False] * N] for _ in range(N)]
  
  queue = deque
  queue.append((sharkX,sharkY,0))  
  visited[sharkX][sharkY] = 1
  
  while True:    
    x,y,cnt = queue.popleft()
    for i in range(4):
      dx = x + pos[i][0]
      dy = y + pos[i][1]

      if 0 <= dx < N and 0 <= dy <N:
        graph[dx][dy] <= shark
        
EatFish = 0
while True:
  value = bfs()