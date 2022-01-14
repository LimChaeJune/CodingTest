import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

queue = deque()
for i in range(N):
    items = input().split()

    if items[0] == 'push_back':
        queue.append(items[1])           
    
    elif items[0] == 'push_front':
        queue.appendleft(items[1])   

    elif items[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif items[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif items[0] == 'size':        
        print(len(queue))
    elif items[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif items[0] == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif items[0] == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    