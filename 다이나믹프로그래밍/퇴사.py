N = int(input())
days = []
dp = [0 for i in range(N+1)]

for i in range(N):
    t, p = map(int, input().split())
    days.append((t, p))

for i in range(N-1, -1, -1):
    if i + days[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], days[i][1] + dp[i + days[i][0]])

print(dp[0])


# 그 날 일을 안했다고해서 dp[i]에 0을 넣는것이 아니라, 이전까지 일해서 받을 수 있던 최댓값인 dp[i+1] 넣어야 함
