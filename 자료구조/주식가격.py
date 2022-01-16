prices = list(map(int, input().split()))

res = []

for i in range(len(prices)):
    item = prices[i]
    result = 0
    for j in range(i+1,len(prices)):
        result += 1
        if prices[j] < prices[i]:
            break

    res.append(result)

print(res)

    
