def solution(rows, columns, queries):
    
    board = [[i + (j*columns) for i in range(1, columns+1)] for j in range(rows)]
    answer = []
    
    for query in queries:
        x1, y1 = query[0], query[1]
        x2, y2 = query[2], query[3]
        
        contain = board[x1-1][y1-1]
        
        minDt = 100000
        
        for i in range(y1, y2):
            copys = board[x1-1][i]
            board[x1-1][i] = contain            
            contain = copys            
            minDt = min(minDt, contain) 
            
        
        for i in range(x1, x2):            
            copys = board[i][y2-1]
            board[i][y2-1] = contain            
            contain = copys            
            minDt = min(minDt, contain) 
        
        for i in range(y2-2, y1-2, -1):            
            copys = board[x2-1][i]
            board[x2-1][i] = contain            
            contain = copys            
            minDt = min(minDt, contain) 
        
        for i in range(x2-2, x1-2, -1):            
            copys = board[i][y1-1]
            board[i][y1-1] = contain            
            contain = copys            
            minDt = min(minDt, contain) 
        
        answer.append(minDt)                        
                
    return answer

print(solution(6,6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))