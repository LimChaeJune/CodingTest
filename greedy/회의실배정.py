N = int(input())

array = [[0 for col in range(2)] for row in range(N)]
for i in range(0,N):
  start, end = map(int,(input().split()))
  array[i][0] = start
  array[i][1] = end

array.sort(key = lambda x:x[0])
array.sort(key = lambda x:x[1])

result = 1
end_time = array[0][1]
for j in range(1, N):
  if array[j][0] >= end_time :
    result += 1
    end_time = array[j][1]

print(result)
