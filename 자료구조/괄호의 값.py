from operator import truediv
import sys
input = sys.stdin.readline

vals = list(input().replace('\n',''))
current = list()

pluses = []
result= 0
tmp = 1

while vals:
    i = vals.pop()                
        
    if i == ']':
        tmp *= 3
        pluses.append(i)
    elif i == ')':
        tmp *= 2
        pluses.append(i)
    
    elif i == '(':       
        if not pluses : 
            result = 0
            break

        j = pluses.pop()         
        if j == ']':
            result = 0
            break
        if j == ')'  :
            result += tmp

        tmp //= 2

    elif i == '[':
        if not pluses : 
            result = 0
            break
        
        j = pluses.pop() 
        if j == ')':
            result = 0
            break
        if j == ']':
            result += tmp

        tmp //= 3

print(result)          

