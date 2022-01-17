import math

N = int(input())
M = int(input())

arr = []

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True    

for i in range(N, M+1):     
    if i != 1:
        if is_prime_number(i) :
            arr.append(i)

if len(arr) > 0 :
    print(sum(arr))
    print(min(arr))
else:    
    print(-1)
