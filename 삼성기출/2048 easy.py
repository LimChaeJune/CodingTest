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
    
    if cnt == 6:
        return        

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
                    if thisBoard[i][check] == 0: continue 

                    elif thisBoard[i][check] > 0:
                        if thisBoard[i][j] == thisBoard[i][check] :
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
                
                for check in range(j-1, -1, -1):                        
                    if thisBoard[i][check] == 0:continue      
                                  
                    elif thisBoard[i][check] > 0:
                        if thisBoard[i][j] == thisBoard[i][check]:
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
                    if thisBoard[check][i] == 0:continue  

                    elif thisBoard[check][i] > 0:
                        if thisBoard[j][i] == thisBoard[check][i]:
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

                for check in range(j-1, -1, -1):    
                    if thisBoard[check][i] == 0: continue  

                    elif thisBoard[check][i] > 0:
                        if thisBoard[j][i] == thisBoard[check][i]:
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

    newBoard1 = [[thisBoard[i][j] for j in range(len(thisBoard))] for i in range(len(thisBoard))]
    newBoard2 = [[thisBoard[i][j] for j in range(len(thisBoard))] for i in range(len(thisBoard))]
    newBoard3 = [[thisBoard[i][j] for j in range(len(thisBoard))] for i in range(len(thisBoard))]
    newBoard4 = [[thisBoard[i][j] for j in range(len(thisBoard))] for i in range(len(thisBoard))]
    dfs(newBoard1, 'L', cnt+1)   
    dfs(newBoard2, 'R', cnt+1)   
    dfs(newBoard3, 'U', cnt+1)   
    dfs(newBoard4, 'D', cnt+1)    

    
pos = ['L','R','U','D']

maxResult = 0

visitedBoard = [[board[i][j] for j in range(len(board))] for i in range(len(board))]



for mypo in pos:
    visitedBoard = [[board[i][j] for j in range(len(board))] for i in range(len(board))]

    dfs(visitedBoard, mypo, 1)

print(maxResult)


