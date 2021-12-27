from collections import deque

M, N = map(int, input().split())

graph = []
queue = deque()
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if graph[i][j] == 1 :
            queue.append((i,j))
            

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():        
    while(queue):
        x, y = queue.popleft()                                                        

        for i in range(4):
            fx = x + dx[i]
            fy = y + dy[i]                  
                
            if N > fx >= 0 and M > fy >= 0 and graph[fx][fy] == 0:
                graph[fx][fy] = graph[x][y] + 1
                queue.append((fx,fy))                    

bfs()

result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
        result = max(result, graph[i][j])

print(result -1)
        
        