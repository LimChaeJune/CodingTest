people = int(input())
times = list(map(int, input().split()))
times.sort()
result = 0
timeadd =0
for time in times:    
    timeadd += time
    result += timeadd

print(result)
