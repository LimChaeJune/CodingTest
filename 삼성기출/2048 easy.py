from ast import If
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

board = [[0 for _ in range(N)] for i in range(N)]

for i in range(N):
    vals = list(map(int, input().split()))
    for j in range(len(vals)):
        board[i][j] = vals[j]



def dfs(thisBoard, thisPos, cnt):    
    global maxResult    
    if thisPos == 'L':
        for i in range(N):
            queue = deque()
            for j in range(N):                                            
                if thisBoard[i][j] == 0:
                    continue  
                
                elif j == N-1:         
                    queue.append(thisBoard[i][j])           
                    continue

                for check in range(j+1, N):
                    if thisBoard[i][check] == 0:
                        continue  
                    elif thisBoard[i][j] == thisBoard[i][check]:
                        thisBoard[i][j] += thisBoard[i][check]    
                        thisBoard[i][check] = 0  
                        break                                      

                queue.append(thisBoard[i][j])
            
            for k in range(N):
                if queue:
                    value = queue.popleft()
                    thisBoard[i][k] = value
                    maxResult = max(maxResult,value)
                else:
                    thisBoard[i][k] = 0      

    elif thisPos == 'R':
        for i in range(N):
            queue = deque()
            for j in range(N-1, -1, -1):                                            
                if thisBoard[i][j] == 0:
                    continue  
                
                elif j == 0:         
                    queue.append(thisBoard[i][j])           
                    continue
                
                for check in range(N-2, -1, -1):    
                    if thisBoard[i][check] == 0:
                        continue
                    elif thisBoard[i][j] == thisBoard[i][check]:
                        thisBoard[i][j] += thisBoard[i][check]                    
                        thisBoard[i][check] = 0
                        break

                queue.append(thisBoard[i][j])
            
            if queue:
                for k in range(N-1, -1, -1):
                    if queue:
                        value = queue.popleft()
                        thisBoard[i][k] = value
                        maxResult = max(maxResult,value)
                    else:
                        thisBoard[i][k] = 0    


    elif thisPos == 'U':
        for i in range(N):
            queue = deque()
            for j in range(N):                                            
                if thisBoard[j][i] == 0:
                    continue  
                
                elif j == N-1:         
                    queue.append(thisBoard[j][i])           
                    continue

                for check in range(j+1, N):
                    if thisBoard[check][i] == 0:
                        continue  
                    elif thisBoard[j][i] == thisBoard[check][i]:
                        thisBoard[j][i] += thisBoard[check][i]      
                        thisBoard[check][i] = 0
                        break     

                queue.append(thisBoard[j][i])
                
            if queue:
                for k in range(N):
                    if queue:
                        value = queue.popleft()
                        thisBoard[k][i] = value
                        maxResult = max(maxResult,value)
                    else:
                        thisBoard[k][i] = 0      

    elif thisPos == 'D':
        for i in range(N):
            queue = deque()
            for j in range(N-1, -1, -1):                                            
                if thisBoard[j][i] == 0:
                    continue  
                
                elif j == 0:         
                    queue.append(thisBoard[j][i])           
                    continue

                for check in range(N-2, -1, -1):    
                    if thisBoard[check][i] == 0:
                        continue  
                    elif thisBoard[j][i] == thisBoard[check][i]:
                        thisBoard[j][i] += thisBoard[check][i]      
                        thisBoard[check][i] = 0
                        break    

                queue.append(thisBoard[j][i])
            
            if queue:
                for k in range(N-1, -1, -1):
                    if queue:
                        value = queue.popleft()
                        thisBoard[k][i] = value
                        maxResult = max(maxResult,value)
                    else:
                        thisBoard[k][i] = 0                            
                            

    if cnt < 5:
        for po in pos:
            dfs(thisBoard, po, cnt+1)   
    
pos = ['L','R','U','D']

maxResult = 0


for mypo in pos:
    visitedBoard = [[board[i][j] for j in range(len(board))] for i in range(len(board))]

    dfs(visitedBoard, mypo, 1)

print(maxResult)


