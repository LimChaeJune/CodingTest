from collections import deque

N, L, R = list(map(int,input().split()))

countires = []

for i in range(N):
    countires.append(list(map(int,input().split())))

pos = [(0,1), (1,0), (-1,0), (0, -1)]

def bfs(x,y,visit):    
    queue = deque()
    connection = []    
    people = 0

    queue.append((x,y))                                
    connection.append((x,y))
    people += countires[x][y]
    visit[x][y] = True  

    while(queue):
        x, y = queue.popleft()             
        
        for po in pos:
            dx = x + po[0]
            dy = y + po[1]
            if dx <= -1 or dx >= N or dy <= -1 or dy >= N or visit[dx][dy]:
                continue            

            if R >= abs(countires[dx][dy] - countires[x][y]) >= L:                
                queue.append((dx,dy))                                
                connection.append((dx,dy))
                people += countires[dx][dy]
                visit[dx][dy] = True                                             

    if (len(connection) == 1):
        return False        

    for x, y in connection:
        countires[x][y] = people // len(connection)
    
    return True

result = 0

while True:
    stop = True    
    c_visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not c_visited[i][j]:
                check = bfs(i,j, c_visited)                    
                if check:
                    stop = False                

    if stop:
        break       
    else:             
        result += 1    

print(result)