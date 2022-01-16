from collections import deque
import math

N = int(input())

for i in range(N):
    cnt, ord = map(int, input().split())
    prints = deque(list(map(int, input().split())))
    hq = deque(list(range(cnt)))
        
    idx = 0
    cnt = 0
    while(hq):        
        if prints[0] == max(prints):                        
            prints.popleft()
            cnt += 1

            if hq.popleft()  == ord:
                print(cnt)
        else:            
            prints.append(prints.popleft())
            hq.append(hq.popleft())
    
