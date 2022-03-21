from collections import deque

def solution(progresses, speeds):
    answer = []
    
    day = 1    
    idx  = 0
    
    queue = deque()
    queue.append((1,0))        
    
    cnt = 0
    while queue:
        day, idx = queue.popleft()                   
        
        if progresses[idx] + (speeds[idx] * day) >= 100:                    
            cnt += 1
            
            for i in range(idx+1, len(progresses)):            
                if progresses[i] + (speeds[i] * day) >= 100:
                    cnt += 1
                else: 
                    queue.append((day, i))                   
                    
                    break             
                
            answer.append(cnt)                    
            cnt = 0
        else:
            queue.append((day+1,idx))
                                                    
    
    return answer

solution([93, 30, 55],[1, 30, 5])