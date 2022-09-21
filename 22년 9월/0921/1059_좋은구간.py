import sys
sys.stdin = open("1059_좋은구간.txt")

T = int(input())

for t in range(T):
    L = int(input())                        # 집합 S의 크기
    lst = list(map(int,input().split()))    # S에 포함된 L개의 정수
    n = int(input())                        # 좋은 구간에 포함되어야 할 n
    lst.sort()

    if n in lst:
        cnt = 0

    elif n < min(lst):
        alpha = 1
        beta = min(lst) - 1

        if alpha == beta:
            cnt = 0
        elif alpha < n < beta:
            cnt = (n - alpha) * (beta - n) + (n - alpha) + (beta - n)
        elif n == alpha:
            cnt = beta - n
        elif n == beta:
            cnt = n - alpha


    else:
        min_elts = []
        max_elts = []
        for elt in lst:
            if elt < n:
                min_elts.append(elt)
            else:
                max_elts.append(elt)

        alpha = min_elts[-1] + 1
        beta = max_elts[0] - 1

        if alpha == beta:
            cnt = 0
        elif alpha < n < beta:
            cnt = (n - alpha)*(beta - n) + (n - alpha) + (beta - n)
        elif n == alpha:
            cnt = beta - n
        elif n == beta:
            cnt = n - alpha
    print(cnt)