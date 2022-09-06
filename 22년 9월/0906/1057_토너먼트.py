import sys
sys.stdin = open("1057_토너먼트.txt")

T = int(input())

for t in range(T):
    N, A, B = map(int,input().split())
    C = min(A, B)
    D = max(A, B)
    cnt = 1
    while D - C > 0:
        if D - C == 1 and C % 2:
            break

        if C % 2:
            C = C//2 + 1
        else:
            C = C//2

        if D % 2:
            D = D//2 + 1
        else:
            D = D//2

        cnt += 1
    print(cnt)