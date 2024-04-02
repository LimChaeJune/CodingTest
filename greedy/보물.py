N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
resultA = [-1] * N

for j in range(N):
    idx = -1
    maxVal = -1000000000
    for i in range(N):
        if resultA[i] != -1: continue
            
        if B[i] > maxVal:
            maxVal = B[i]
            idx = i
     
    resultA[idx] = A[j]

result = 0
for i in range(N):    
    result += (resultA[i] * B[i])

print(result)