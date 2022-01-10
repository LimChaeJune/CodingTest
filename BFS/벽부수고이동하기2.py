from collections import deque
import sys

def bfs(graph, x,y):
    visited = [[[9876543210 for _ in range(M)]for _ in range(N)] for _ in range(K+1)]
    
    queue = deque()
    queue.append((x,y, 1, 0))        
    visited[0][0][0] = 1

    while(queue):
        x, y, cnt, bk = queue.popleft()
        

        if x == (N-1) and y == (M-1):
            return print(cnt)

        for XX, YY in pos:
            dx = x + XX
            dy = y + YY
                                    
            if 0 <= dx < N and 0 <= dy < M :
                if visited[bk][dx][dy] > cnt + 1:                
                    if graph[dx][dy] == '0':              
                        visited[bk][dx][dy] = cnt + 1
                        queue.append((dx, dy, cnt + 1, bk))

                    elif graph[dx][dy] == '1' and bk + 1 <= K:
                        if visited[bk+1][dx][dy] > cnt + 1:
                            visited[bk+1][dx][dy] = cnt + 1
                            queue.append((dx, dy, cnt + 1, bk +1))                
        
    return print(-1)    

N, M, K = map(int, sys.stdin.readline().split())

graph = []
for j in range(N):   
    graph.append(sys.stdin.readline().rstrip())

pos = [(1,0),(0,1),(-1,0),(0,-1)]

bfs(graph,0,0)