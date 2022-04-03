import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for i in range(N):  
  graph.append(list(map(int, input().split())))

move = []

for i in range(M):
  move.append(list(map(int, input().split())))

# 구름 위치 인덱스 -1 해줘야함
pos = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]

cloudboard = [[0 for j in range(N)]for i in range(N)]
cloudboard[N-1][0] = 1
cloudboard[N-1][1] = 1
cloudboard[N-2][0] = 1
cloudboard[N-2][1] = 1

for i in range(len(move)):
  d,s = move[i]  
  d = d-1  
  visited = []
    
  # 구름 있는 그래프 탐색
  for r in range(N):
    for c in range(N):
      if cloudboard[r][c] == 1:
        dx = r
        dy = c
        for sec in range(s):
          dx = dx + pos[d][0]
          dy = dy + pos[d][1]
          # 인덱스가 넘어가면 다음 열로 넘어가게 처리
          if dx >= N:
            dx = 0
          elif dx < 0:
            dx = N-1
          if dy >= N:
            dy = 0
          elif dy < 0:
            dy = N-1        
        # 물양 증가 시켜주기        
        graph[dx][dy] += 1       
        
        # 대각선 로직 처리 위해서
        cloudboard[r][c] = 0        
        
        # 5번 조건 3에서 구름이 사라지는 칸이 아니여야함
        visited.append((dx,dy))

   # 대각선 거리 1인 칸 물양 추가 증가 
  for vis in range(len(visited)):
      r, c = visited[vis]
      cnt = 0

      if r-1 >= 0 and c-1 >= 0:
            if graph[r-1][c-1] > 0:
                cnt += 1
      if r-1 >= 0 and c+1 < N:
            if graph[r-1][c+1] > 0:
                cnt += 1
      if r+1 < N and c-1 >= 0:
            if graph[r+1][c-1] > 0:
                cnt += 1
      if r+1 < N and c+1 < N:
            if graph[r+1][c+1] > 0:
                cnt += 1

      graph[r][c] += cnt

  # 바구니 확인하면서 물 있는 것은 구름 만들어준다.
  for r in range(N):
    for c in range(N):
      if graph[r][c] >= 2 and (r,c) not in visited:
        graph[r][c] -= 2
        cloudboard[r][c] = 1
        
# 결과 확인
answer = 0
for r in range(N):
  for c in range(N):
    if graph[r][c] > 0:
      answer += graph[r][c]
    
print(answer)
