import sys
sys.stdin = open("1264_모음의개수.txt")

for _ in range(10000):
    N = list(map(str,input()))
    cnt = 0
    if N == ['#']:
        break
    else:
        for elt in N:
            if elt in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
                cnt += 1
    print(cnt)