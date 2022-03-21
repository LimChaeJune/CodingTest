from math import gcd
def solution(w,h):
    answer = 1
    
    boxs = w * h
    answer = boxs - ((w+h) - gcd(w,h))
    
    return answer