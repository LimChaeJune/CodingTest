from collections import deque
import sys
input = sys.stdin.readline

polio = [
    [[1,0,0,0]
    ,[1,0,0,0]
    ,[1,0,0,0]
    ,[1,0,0,0]],
    
    [[1,1,1,1]
    ,[0,0,0,0]
    ,[0,0,0,0]
    ,[0,0,0,0]],

    [[1,0,0,0]
    ,[1,0,0,0]
    ,[1,1,0,0]
    ,[0,0,0,0]],

    
    [[0,1,0,0]
    ,[0,1,0,0]
    ,[1,1,0,0]
    ,[0,0,0,0]],

    [[1,1,0,0]
    ,[1,0,0,0]
    ,[1,0,0,0]
    ,[0,0,0,0]],

    [[1,1,0,0]
    ,[0,1,0,0]
    ,[0,1,0,0]
    ,[0,0,0,0]],

    [[1,1,1,0]
    ,[1,0,0,0]
    ,[0,0,0,0]
    ,[0,0,0,0]],

    [[1,0,0,0]
    ,[1,1,1,0]
    ,[0,0,0,0]
    ,[0,0,0,0]],

    [[1,1,1,0]
    ,[0,0,1,0]
    ,[0,0,0,0]
    ,[0,0,0,0]],

    [[0,0,1,0]
    ,[1,1,1,0]
    ,[0,0,0,0]
    ,[0,0,0,0]],

    [[1,0,0,0]
    ,[1,1,0,0]
    ,[0,1,0,0]
    ,[0,0,0,0]],

    [[1,0,0,0]
    ,[1,1,0,0]
    ,[0,1,0,0]
    ,[0,0,0,0]],

    [[0,1,0,0]
    ,[1,1,0,0]
    ,[1,0,0,0]
    ,[0,0,0,0]],

    [[1,1,0,0]
    ,[0,1,1,0]
    ,[0,0,0,0]
    ,[0,0,0,0]],

    [[0,1,1,0]
    ,[1,1,0,0]
    ,[0,0,0,0]
    ,[0,0,0,0]],

    
    [[1,1,1,0]
    ,[0,1,0,0]
    ,[0,0,0,0]
    ,[0,0,0,0]],

    [[0,1,0,0]
    ,[1,1,1,0]
    ,[0,0,0,0]
    ,[0,0,0,0]],

    [[1,0,0,0]
    ,[1,1,0,0]
    ,[1,0,0,0]
    ,[0,0,0,0]],

    [[0,1,0,0]
    ,[1,1,0,0]
    ,[0,1,0,0]
    ,[0,0,0,0]],

    [[1,1,0,0]
    ,[1,1,0,0]
    ,[0,0,0,0]
    ,[0,0,0,0]],
]

N, M = map(int, input().split()) 

graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))

pos = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs():
    global result
    myqueue = deque()
    myqueue.append((0,0))    
    visted = [[0 for _ in range(M)] for _ in range(N)]
    visted[0][0] = 1

    while myqueue:
        x, y = myqueue.popleft()

        for pol in polio:    
            val = 0
            isDone = False
            for row in range(4):
                for col in range(4):
                    if pol[row][col] == 0: continue

                    if 0 <= x + row < N and 0 <= y + col < M : 
                        val += graph[x+row][y+col]
                    else: 
                        isDone = True
                        break
                if isDone:
                    break
            
            if isDone:
                continue

            result = max(result, val)
            

        for po in pos:
            dx = x + po[0]
            dy = y + po[1]            

            if 0 <= dx < N and 0 <= dy < M and visted[dx][dy] == 0:
                myqueue.append((dx,dy))        
                visted[dx][dy] = 1
            


result = 0

bfs()
print(result)

