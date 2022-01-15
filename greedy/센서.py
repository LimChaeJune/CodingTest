import math

N = int(input())

for i in range(N):
    cnt, ord = map(int, input().split())
    prints = list(map(int, input().split()))

    hq = []        

    for i in range(len(prints)):
        hq.append(prints[i])

    result = 0    
    idx = 0

    while(hq):        
        if max(hq) == hq[idx] :            
            hq.pop(hq[idx])
        else:
            data = hq[idx]
            hq.remove(hq[idx])
            hq.append(hq[idx])

    print(result)
