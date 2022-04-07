N = int(input())
graph = []

for i in range(N):
  graph.append(list(map(int, input().split())))

def div(x,y):  
  global graph

  Danswer = 1e9

  # i가 d1 / j가 d1
  # 기준점과 경계 길이 설정 가능한지
  for i in range(1,N):
    if i + x >= N or y-i >= y or y-i < 0:
      continue
    for j in range(1, N):
        if x >= x+i+j or x + i + j >= N or y + j >= N:
          continue

        newboard = [[0 for _ in range(N)] for _ in range(N)]
                    

        # 경계선 그리기
        for l1 in range(i+1):
            newboard[x+l1][y-l1] = 5
        # 경계선 그리기
        for l2 in range(j+1):
            newboard[x+l2][y+l2] = 5
        # 경계선 그리기
        for l3 in range(j+1):
            newboard[x+i+l3][y-i+l3] = 5            
        # 경계선 그리기
        for l4 in range(i+1):
            newboard[x+j+l4][y+j-l4] = 5
        
        
        # 경계선 사이 채우기
        for st1 in range(x+1, x+j+i):            
            st_check = -1
            fns_check = -1
            for ch in range(N):
                if st_check == -1 and newboard[st1][ch] == 5:
                    st_check = ch
                elif st_check > -1 and newboard[st1][ch] == 5:
                    fns_check = ch

            if st_check > -1 and fns_check > -1:
                for st2 in range(st_check+1, fns_check):
                    newboard[st1][st2] = 5     

        part1, part2, part3, part4, part5 = 0,0,0,0,0   

        for f in range(N):
            for f2 in range(N):
                if newboard[f][f2] == 5:
                    part5 += graph[f][f2]
        
        # 선거구 1    
        for p1 in range(x+i):
            for pp1 in range(y+1):
                if newboard[p1][pp1] == 0:
                    newboard[p1][pp1] = 1
                    part1 += graph[p1][pp1]
            
        # 선거구 2    
        for p2 in range(x+j+1):
            for pp2 in range(y+1, N):
                if newboard[p2][pp2] == 0:
                    newboard[p2][pp2] = 2
                    part2 += graph[p2][pp2]

        # 선거구 3        
        for p3 in range(x+i, N):
            for pp3 in range(y-i+j):
                if newboard[p3][pp3] == 0:
                    newboard[p3][pp3] = 3
                    part3 += graph[p3][pp3]
            
        # 선거구 4        
        for p4 in range(x+j, N):
            for pp4 in range(y-i+j, N):
                if newboard[p4][pp4] == 0:
                    newboard[p4][pp4] = 4
                    part4 += graph[p4][pp4]

        # 하나의 선거구를 가지고있어야 됨
        if part1 == 0 or part2 == 0 or part3 == 0 or part4 == 0 or part5 == 0:
            continue                

        minVal = min(part1, part2, part3, part4, part5)
        maxVal = max(part1, part2, part3, part4, part5)
        Danswer = min(Danswer, maxVal - minVal)

  return Danswer

answer = 1e9
for k in range(N):
    for kk in range(N):
       answer = min(answer, div(k,kk))

print(answer)