N, L = map(int, input().split())

loads = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
  loadValue = list(map(int, input().split()))
  for j in range(len(loadValue)):
    loads[i][j] = loadValue[j]

result = 0

def dfs(x, y, type, con, uphill, isUp): 
    global result    

    if type == 'row':
        if x == N-1:
            result += 1
            return True

        dx = x + 1
        if loads[dx][y] == loads[x][y]:
            if isUp > 0 : 
                isUp -= 1
                con = 1
            else : con += 1
            dfs(dx, y, type,con, uphill, isUp)
        elif loads[dx][y] > loads[x][y]:
            if isUp > 0 or loads[dx][y] - loads[x][y] > 1:
               return False
            if con >= uphill:
               dfs(dx,y,type,1,uphill, 0)
        elif loads[dx][y] < loads[x][y]:
            check = False
            if N - dx >= uphill:
                stVal = 1
                if loads[x][y] - loads[dx][y] == 1:
                    while True:                                   
                        if stVal == L : 
                            check = True
                            break

                        if loads[dx][y] == loads[dx+stVal][y]:
                            stVal += 1                    
                        else:                        
                            break
            if check:
                dfs(dx,y,type,1,uphill, L)

    elif type == 'column':
        if y == N-1:
            result += 1
            return True

        dy = y + 1
        if loads[x][dy] == loads[x][y]:
            if isUp > 0 : 
                isUp -= 1
                con = 1
            else : con += 1

            dfs(x, dy, type,con, uphill, isUp)
        elif loads[x][dy] > loads[x][y]:
            if isUp > 0 or loads[x][dy] - loads[x][dy] > 1:
               return False
            if con >= uphill:
               dfs(x,dy,type,1,uphill, 0)
        elif loads[x][dy] < loads[x][y]:
            check = False
            if N - dy >= uphill:
                stVal = 1
                if loads[x][y] - loads[x][dy] == 1:
                    while True:                                   
                        if stVal == L : 
                            check = True
                            break
                        
                        if loads[x][dy] == loads[x][dy+stVal]:
                            stVal += 1                    
                        else:                        
                            break
            if check:
                dfs(x,dy,type,1,uphill, L)
            


for i in range(N):
    dfs(0,i,'row',1,L, 0)
    dfs(i,0,'column',1,L, 0)


print(result)
   