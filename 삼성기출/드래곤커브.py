from collections import deque

N = int(input())
board = [[0 for _ in range(101)] for _ in range(101)]
curbes = []

for i in range(N):    
    curbes.append(list(map(int,input().split())))

pos = [[1,0],[0,-1],[-1,0],[0,1]]
changePos = [1,2,3,0]

def curbeDraw(x,y,d,g):         
    queue = deque()
    queue.append((x,y,d,g,1))

    visited = []
    while(queue):
        x,y,d,g,curbe = queue.popleft()        
        
        if curbe == 1:
            board[y][x] = 1

            x = x + pos[d][0]
            y = y + pos[d][1]

            board[y][x] = 1

            visited.append(d)
        elif curbe > 1:            
            board[y][x] = 1

            newvalue = []
            for i in range(len(visited)-1, -1, -1):
                value = visited[i]

                change = changePos[value]
                x = x + pos[change][0]
                y = y + pos[change][1]             

                board[y][x] = 1
                newvalue.append(change)
            
            for j in newvalue:
                visited.append(j)            

        if curbe <= g:
            queue.append((x,y,d,g,curbe+1))        
                                                          

for i in range(N):
    curbe = curbes[i]
    curbeDraw(curbe[0],curbe[1],curbe[2],curbe[3])    

cubes = 0
for row in range(100):
    for column in range(100):              
        if board[row][column] == 1 and board[row][column+1] == 1 and board[row+1][column] ==1  and board[row+1][column+1] == 1:
            cubes += 1


print(cubes)
    


