

stack = []

N = int(input())

for i in range(N):
    items = input().split()

    if items[0] == 'push':
        stack.append(items[1])           
    elif items[0] == 'top':
        if len(stack) == 0:
            print(-1)
        print(stack[-1])
    elif items[0] == 'size':        
        print(len(stack))
    elif items[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif items[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    