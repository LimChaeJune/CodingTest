N = int(input())
sol = list(map(int,input().split()))

sol.reverse()

dp = [1] * N

for i in range(1,N):
    for j in range(0, i):
        if dp[j] < dp[i]:
            dp[i] = max(dp[i], dp[j] + 1)


print(N - max(dp))