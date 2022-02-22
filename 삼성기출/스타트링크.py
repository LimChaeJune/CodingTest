from itertools  import combinations

N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]
NtoVal = [i for i in range(N)]

for i in range(N):
  val = list(map(int, input().split()))
  for j in range(len(val)):
    graph[i][j] = val[j]

combis = []

for i in combinations(NtoVal, N // 2):
  combis.append(i)

result = 10000

for i in range(len(combis)):
  team1 = combis[i]
  team1Val = 0
  for j in range(N // 2):
    val1 = team1[j]
    for k in team1:
      team1Val += graph[val1][k]

  team2Val = 0
  team2 = combis[-i-1]  
  
  for j in range(len(team2)):
      val1 = team2[j]
      for k in team2:
        team2Val += graph[val1][k]

  result = min(result, abs(team1Val - team2Val))

print(result)
  