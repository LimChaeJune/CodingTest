
R, C, T = map(int, input().split())

graph = [[0 for _ in range(C)] for _ in range(R)]
machine = []
smog = []

for i in range(R):
  row = list(map(int, input().split()))
  for r in range(len(row)):
    graph[i][r] = row[r]
    if row[r] == -1:
      machine.append((i, r))

posx = [1, -1, 0, 0]
posy = [0, 0, 1, -1]    
   

        
for i in range(T):
    new = [[0 for _ in range(C)] for _ in range(R)]

    for r in range(R):
      for c in range(C):
        if graph[r][c] >= 5:
          # 확산 값
          value = graph[r][c] // 5

          # 나눠준 수
          cnt = 0

          for i in range(4):
            dx = r + posx[i]
            dy = c + posy[i]
            if 0 <= dx < R and 0 <= dy < C and graph[dx][dy] != -1:              
              new[dx][dy] += value
              cnt += 1

          graph[r][c] = graph[r][c] - value * cnt

    for r in range(R):
      for c in range(C):
          graph[r][c] += new[r][c]

     # upper bound (반시계)
    x1, y1 = machine[0][0], machine[0][1]
    x2, y2 = machine[1][0], machine[1][1]    

    temp = graph[x1][C-1]
    for i in range(C-2, 0, -1):
      graph[x1][i+1] = graph[x1][i]

    temp2 = graph[0][C-1]
    for i in range(x1-1):
      graph[i][C-1] = graph[i+1][C-1]
    graph[x1-1][C-1] = temp

    temp = graph[0][0]
    for i in range(C-1):
      graph[0][i] = graph[0][i+1]
    graph[0][C-2] = temp2

    for i in range(x1-1, 1 -1):
      graph[i][0] = graph[i-1][0]
    graph[x1][1] = 0
    graph[1][0] = temp

    # lower bound (오 아래 왼 위 순서)
    temp = graph[x2][C-1]
    for i in range(C-2, 0, -1):
        graph[x2][i+1] = graph[x2][i]

    temp2 = graph[R-1][C-1]
    for i in range(R-1, x2, -1):
        graph[i][C - 1] = graph[i-1][C - 1]
    graph[x2+1][C-1] = temp

    temp = graph[R-1][0]
    for i in range(C-1):
        graph[R-1][i] = graph[R-1][i+1]
    graph[R-1][C-2] = temp2

    for i in range(x2+1, R-1):
        graph[i][0] = graph[i+1][0]
    graph[x2][1] = 0
    graph[R-2][0] = temp

answer = 0
for r in range(R):
      for c in range(C):
          if graph[r][c] > 0:              
            answer += graph[r][c]

print(answer)