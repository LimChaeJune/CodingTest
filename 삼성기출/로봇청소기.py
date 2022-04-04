N, M = map(int, input().split())

# 현재 로봇 좌표 / d- 방향
r,c,d = map(int, input().split())

pos = [[-1,0],[0,1],[1,0],[0,-1]]
graph = []

for i in range(N):
  graph.append(list(map(int, input().split())))

# 로봇 회전
def rotate(myd):
  if myd == 0:
    return 3
  else:
    return myd - 1

# 로봇 후진
def returns(myd):
  if myd == 0 or myd == 1:
    return myd+2
  else:
    return myd-2

answer = 0
contCnt = 0
while True:
  if graph[r][c] == 0:
    graph[r][c] = -1
    answer += 1

  if d == 0:
    dx = r + pos[3][0]
    dy = c + pos[3][1]
  else:
    dx = r + pos[d-1][0]
    dy = c + pos[d-1][1]

  if graph[dx][dy] == 0:
    r = dx
    c = dy
    d = rotate(d)
    contCnt = 0
  else:
    d = rotate(d)
    contCnt += 1
  
  if contCnt >= 4:
    returnD = returns(d)
    dx = r + pos[returnD][0]
    dy = c + pos[returnD][1]

    if graph[dx][dy] == 1:
      break
    else:
      r = dx
      c = dy
      contCnt = 0

print(answer)