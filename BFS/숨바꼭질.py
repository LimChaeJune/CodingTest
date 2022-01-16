from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split()) 

graph = [0] * 100002

def avg(ag,data):
    if ag == 0: data += 1
    elif ag == 1: data -= 1
    elif ag == 2: data *= 2

    return data

def bfs():                    
    queue = deque()
    queue.append((N,1))    
    graph[N] = 1

    while queue:         
        st, cnt = queue.popleft()        

        if st == K:
            print(graph[K]-1)
            break

        for i in range(3):                        
            dx = avg(i,st)

            if dx < 0 or dx > 100001  : continue

            if graph[dx] == 0 :                 
                queue.append((dx, cnt+1))     
                graph[dx] = cnt+1
            
bfs()                                                