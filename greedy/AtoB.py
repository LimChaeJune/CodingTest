A,B = map(int,input().split())

result = 1

while(True):
    if B == A:        
        break
    elif (B % 2 != 0 and B % 10 != 1) or (B < A):        
        result = -1
        break
    else:
        if B % 10 == 1:
            B = B // 10
            result = result + 1
        elif B % 2 == 0 :
            B = B // 2
            result = result + 1


print(result)