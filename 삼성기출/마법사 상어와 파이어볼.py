N,M,K = map(int, input().split())

board = [[[] for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
  fb = list(map(int,input().split()))
  # x,y,질량,속력,방향
  board[fb[0]][fb[1]].append((fb[2],fb[3],fb[4]))

# 방향 8개
pos = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
# 나눈거 방향
fpos = [(0,2,4,6),(1,3,5,7)]
def action():
  new = [[[] for _ in range(N+1)] for _ in range(N+1)]

  # 방향으로 속력 만큼 이동한다.
  for i in range(1, N+1):
    for j in range(1, N+1):
      if len(board[i][j]) > 0:
        for k in board[i][j]:                                        
          # 방향
          id = k[2]
          
          pattern = k[1]
          if pattern >= N:
              pattern = k[1] % N

          dx = i
          dy = j
          # 속력만큼 이동해주기 위해 반복
          for _ in range(pattern):            
            dx = dx + pos[id][0]
            dy = dy + pos[id][1]

            if dx < 1 and pos[id][0] < 0:
                dx = N
            elif dx > N and pos[id][0] > 0:
                dx = 1

            if dy < 1 and pos[id][1] < 0:
                dy = N            
            elif dy > N and pos[id][1] > 0:
                dy = 1                                                             
          
          new[dx][dy].append(k)

  new2 = [[[] for _ in range(N+1)] for _ in range(N+1)]
  for i in range(1, N+1):
    for j in range(1, N+1):
      if len(new[i][j]) == 1:
        new2[i][j] = new[i][j]
      elif len(new[i][j]) > 1:
        # 합쳐진 질량
        sumM = 0          
        # 합쳐진 속력
        sumS = 0
        # 합쳐진 파이어볼 개수
        sumLen = len(new[i][j])
        # 홀수인지 짝수인지
        isnum1, isnum2 = True, True
        for k in new[i][j]:          
          sumM += k[0]
          sumS += k[1]
          # 방향이 모두 홀수거나 짝수인지 확인
          if k[2] % 2 > 0:
            isnum2 = False
          elif k[2] % 2 == 0:
            isnum1 = False

        # 질량이 0 이면 소멸되서 사라짐
        if sumM // 5  < 1:
          continue      

        myM = sumM // 5        
        myS = sumS // sumLen
        myPos = []
        if isnum1 or isnum2:
          myPos = fpos[0]
        else:
          myPos = fpos[1]
        
        for po in myPos:          
          new2[i][j].append((myM, myS, po))

  for i in range(1, N+1):
    for j in range(1, N+1):
      board[i][j] = new2[i][j]
  

for _ in range(K):
  action()

answer = 0
for i in range(1, N+1):
  for j in range(1, N+1):
    if len(board[i][j]) > 0:
      for val in board[i][j]:
        answer += val[0]

print(answer)
  
            
                        
          
            
  