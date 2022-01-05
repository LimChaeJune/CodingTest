from collections import deque
from sys import flags


pos = [(1,2), (1, -2), (-1, 2), (-1 , -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]   

T  = int(input())

result = []

for i in range(T):    
    j = int(input())    
    graph = [[0 for o in range(j)] for k in range(j)]    
    st_X, st_Y  = list(map(int, input().split()))
    targetX,targetY = list(map(int, input().split()))
    
    queue = deque()
    queue.append((st_X, st_Y))

    while queue:
        x, y = queue.popleft()

        if x == targetX and y == targetY:
            result.append(graph[targetX][targetY])
            break
        
        for po in pos:
            nx = x + po[0]
            ny = y + po[1]

            if (len(graph) <= nx) or (nx < 0) or (len(graph) <= ny) or (ny < 0) or graph[nx][ny] > 0:
                continue
                    
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

            if nx == targetX and ny == targetY :                 
                break

        

for rel in result:
    print(rel)
    

    
