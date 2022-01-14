from itertools import combinations, permutations

items = list(map(int, input().split(',')))

def is_prime_number(x):    
    for i in range(2, x):        
        if x % i == 0:
            return False 
    return True 


def solution(nums):
    checks = list(combinations(nums,3))

    result = 0
    for i in checks:
        if is_prime_number(i[0] + i[1] + i[2]):
            result+=1

    return result

print(solution(items))
