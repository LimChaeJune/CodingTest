import graphlib
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    cols = list(map(int,input().split()))
    for col in range(len(cols)):
        graph[i][col] = cols[col]

moving = list(map(int, input().split()))        

dice = []

for i in moving:



