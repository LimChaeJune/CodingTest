n = int(input())

dp = [0] * 123456

def solution(p):        
    if dp[p] != 0:
        return dp[p]

    if 0 < p < 4:        
        dp[p] = 1
        return 1
    elif 3 < p < 6:
        dp[p] = 2      
        return 2    
    else :
        result = solution(p -1)  + solution(p-5)
        dp[p] = result
        return result
        
    

for i in range(n):
    k = int(input())
    res = solution(k)
    print(dp[k])

