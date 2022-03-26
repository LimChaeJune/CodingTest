from collections import deque

xs, ys = map(int, input().split())
xe, ye = map(int, input().split())

port = []


for i in range(3):
    port.append(list(map(int,input().split())))
  

pos = [(1,0),(-1,0),(0,1),(0,-1)]

answer = 0
queue = deque()
queue.append((xs, ys, 0))

visited = []
while queue:
    x, y, cnt = queue.popleft()

    if x == xe and y == ye:
      answer = cnt
      break

    for i in port:
        if i[0] == x and i[1] == y:
            queue.append((i[2], i[3], cnt+10))
            visited.append((x, y))
        elif i[2] == x and i[3] == y:
            queue.append((i[0], i[1], cnt+10))
            visited.append((x, y))   

    for po in pos:
      dx = x + po[0]
      dy = y + po[1]

      if dx < 0 or dy < 0 or (dx, dy) in visited:
        continue
      else:
        queue.append((dx, dy, cnt+1))
        visited.append((dx, dy))                      

print(answer)
