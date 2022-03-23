from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    dicts = defaultdict(int)
    courseMax = defaultdict(int)

    answer = []

    for order in orders:
        items = list(order)        
        for i in course:
            for j in combinations(items, i):
                keys = sorted(j)
                mykey = ''.join(keys)
                dicts[mykey] += 1
                courseMax[i] = max(dicts[mykey], courseMax[i])
    
    

    for key, value in dicts.items():
        if courseMax[len(key)] <= value and value > 1:                    
            answer.append(key)
          
    answer.sort()          
    return answer
