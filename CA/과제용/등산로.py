import sys, pprint
sys.stdin = open("input12.txt","r")

t=int(input())

for tc in range(1,t+1):
    N,K = map(int,input().split())
    matrix=[]
    for _ in range(N):
        matrix.append(list(map(int,input().split())))
    pprint.pprint(matrix)