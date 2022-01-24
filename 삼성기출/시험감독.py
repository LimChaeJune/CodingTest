import sys
input = sys.stdin.readline

N = int(input())

peoples = list(map(int, input().split()))

main, sub = map(int, input().split())

result = 0



for i in peoples:    
  if i <= main:
    result +=1
    continue    
  else:
    i -= main
    result += 1       

    if i < sub :
      result += 1
      
    else:
      result += i // sub              
      if 0 < i % sub < sub:
        result +=1        

print(result)  