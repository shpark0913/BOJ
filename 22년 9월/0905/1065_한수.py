import sys
sys.stdin = open("1065_한수.txt")

T = int(input())

for t in range(T):      # 제출은 7번째 줄부터 할 것
    N = int(input())    # N 이하의 한수를 구해보자구
    c = 0               # 한수의 총 개수를 셀 변수
    lst1 = [i for i in range(1, 10)]
    lst2 = [i for i in range(10, 100)]
    lst3 = []
    for i in range(1, 10):
        for j in range(1, 10):
            k = 2 * j - i
            if 0 <= k < 10:
                num = 100*i + 10*j + k
                lst3.append(num)
    for elt in lst1:
        if elt <= N:
            c += 1
    for elt in lst2:
        if elt <= N:
            c += 1
    for elt in lst3:
        if elt <= N:
            c += 1
    print(c)