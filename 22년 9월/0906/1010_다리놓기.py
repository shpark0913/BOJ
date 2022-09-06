import sys
sys.stdin = open("1010_다리놓기.txt")

def facto(N):
    c = 1
    for i in range(N, 1, -1):
        c *= i
    return c

T = int(input())

for t in range(T):
    N, M = map(int,input().split())   # N : 서쪽의 사이트 수  /  M : 동쪽의 사이트 수
    print(int(facto(M)/(facto(N)*facto(M-N))))