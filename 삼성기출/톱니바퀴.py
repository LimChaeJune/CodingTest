tobni = []
for i in range(4):
   values =  list(input())
   tobni.append(values)

active = []
N = int(input())
for i in range(N):
  k, j = map(int, input().split())
  active.append((k-1, j))

# n-톱니idx, pos 톱니방향,  톱니 회전방향
def dfs(no, rotate, visit):
  visit.append(no)
  
  if no-1 >= 0 and ((no-1) not in visit):
    if tobni[no-1][2] != tobni[no][6]:
      dfs(no - 1, -(rotate),visit)
  if no+1 < 4 and ((no+1) not in visit):
    if tobni[no+1][6] != tobni[no][2]:
      dfs(no + 1, -(rotate),visit)

  if rotate == -1:
    value = tobni[no].pop(0)
    tobni[no].append(value)
  else:
    value = tobni[no].pop()
    tobni[no].insert(0,value)    
        
for j in active:  
  visit = []
  dfs(j[0],j[1], visit)

result = 0
if tobni[0][0] == '1':
    result += 1
if tobni[1][0] == '1':
    result += 2
if tobni[2][0] == '1':
    result += 4
if tobni[3][0] == '1':
    result += 8

print(result)