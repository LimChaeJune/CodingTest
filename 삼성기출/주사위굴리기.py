import sys
input = sys.stdin.readline

N, M, X, Y, mCnt = map(int, input().split())

graph = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    cols = list(map(int,input().split()))
    for col in range(len(cols)):
        graph[i][col] = cols[col]

moving = list(map(int, input().split()))        

# 위, 아래, 오, 왼, 앞, 뒤
dice = [0,0,0,0,0,0]

dy = [0,1,-1,0,0]
dx = [0,0,0,-1,1]


cy = Y
cx = X
for i in moving:               
    if cx + dx[i]  < 0 or cx + dx[i] >= N or cy + dy[i] < 0 or cy + dy[i] >= M:
        continue    

    cy += dy[i]
    cx += dx[i]

    copyDice = dice[:] 

    if i == 1:
        dice[0] = copyDice[3]
        dice[1] = copyDice[2]
        dice[2] = copyDice[0]
        dice[3] = copyDice[1]
    elif i == 2:
        dice[0] = copyDice[2]
        dice[1] = copyDice[3]
        dice[2] = copyDice[1]
        dice[3] = copyDice[0]
    elif i == 3:
        dice[0] = copyDice[4]
        dice[1] = copyDice[5]
        dice[4] = copyDice[1]
        dice[5] = copyDice[0]
    elif i == 4:
        dice[0] = copyDice[5]
        dice[1] = copyDice[4]
        dice[4] = copyDice[0]
        dice[5] = copyDice[1]

    if graph[cx][cy] == 0:
        graph[cx][cy] = dice[1]
    else:
        dice[1] = graph[cx][cy]
        graph[cx][cy] = 0

    print(dice[0])
    


