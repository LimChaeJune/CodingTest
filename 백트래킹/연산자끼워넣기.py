import sys
input = sys.stdin.readline

N = int(input())

items = list(map(int, input().split()))
oper = list(map(int, input().split()))

maxVal = -1000000001
minVal = 1000000001

def dfs(pl,mi,mul,divi, idx, value):        
    global maxVal, minVal    
    
    if idx == N:
        maxVal = max(maxVal, value)    
        minVal = min(minVal, value)        

    if pl > 0:        
        dfs(pl-1,mi,mul,divi,idx+1, value+items[idx])                
    if mi > 0:        
        dfs(pl,mi-1,mul,divi,idx+1, value-items[idx])
    if mul > 0:        
        dfs(pl,mi,mul-1,divi,idx+1, value*items[idx])        
    if divi > 0:
        val = value//items[idx]      
        val2 = value/items[idx]  

        if value < 0 and items[idx] > 0 and val2 > val :
            dfs(pl,mi,mul,divi-1,idx+1, val + 1)
        else:
            dfs(pl,mi,mul,divi-1,idx+1, value//items[idx])            
    


       
dfs(oper[0],oper[1],oper[2],oper[3], 1, items[0])

print(maxVal)
print(minVal)

