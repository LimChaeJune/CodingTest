N, K = map(int, input().split())

coins = []
for _ in range(0,N):
  coins.append(int(input()))

result = 0


for coin in sorted(coins, reverse=True):  
    coincnt =  K // coin 
    K -= coin * coincnt
    result += coincnt
  

print(result)
