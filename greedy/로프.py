import sys

rope = int(sys.stdin.readline())
weight = []

for N in range(rope):
    weight.append(int(sys.stdin.readline()))

weight.sort(reverse=True)
result = 0
for i in range(rope):
    result = max(result, weight[i] * (i + 1)) 

print(result)

