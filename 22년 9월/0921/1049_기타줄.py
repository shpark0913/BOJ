import sys
sys.stdin = open("1049_기타줄.txt")

T = int(input())

for t in range(T):
    N, M = map(int,input().split())  # N : 끊어진 기타줄 수  /  M : 기타줄 브랜드 수
    lst = [list(map(int,input().split())) for _ in range(M)]
    min_pack = 1000
    min_1 = 1000
    for elt in lst:
        if elt[0] < min_pack:
            min_pack = elt[0]
        if elt[1] < min_1:
            min_1 = elt[1]
    print(min((N//6)*min_pack + (N%6)*min_1, N*min_1, (N//6+1)*min_pack))