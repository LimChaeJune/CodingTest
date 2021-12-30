# import sys
# from collections import defaultdict

# T = int(sys.stdin.readline())

# cases = defaultdict(list)

# for case in range(T):
#     N = int(input())
#     for _ in range(N):        
#         cases[case].append(list(map(int, sys.stdin.readline().split())))

# result = []

# for key in cases:
#     group = cases[key]    
#     passCnt = len(group)
#     for item in group:        
#         val1 = item[0]
#         val2 = item[1]
#         for betItem in group:
#             if item == betItem : continue
#             if val1 > betItem[0] and val2 > betItem[1]:
#                 passCnt = passCnt - 1
#                 break
#     result.append(passCnt)

# for res in result:
#     print(res)

# -- 시간초과로 아래꺼로... 포문을 덜 타서 되는 듯.
import sys

T = int(input()) 

for i in range(0,T):
    Cnt = 1
    people = []
    
    N = int(input())
    for i in range(N):
        Paper, Interview = map(int,sys.stdin.readline().split())
        people.append([Paper, Interview])

    people.sort() 
    Max = people[0][1]
    
    for i in range(1,N):
        if Max > people[i][1]:
            Cnt += 1
            Max = people[i][1]

    print(Cnt)