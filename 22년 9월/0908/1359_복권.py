import sys
sys.stdin = open("1359_복권.txt")

def combi(N, M):
    c, d = 1, 1
    for i in range(N, N-M, -1):
        c *= i
    for j in range(M, 1, -1):
        d *= j
    return c//d

##################################################

T = int(input())

for t in range(T):
    N, M, K = map(int,input().split())   # 1~N 중 M개의 수를 선택. 최소 K개가 같으면 당첨

    numerator, denominator = 0, 0        # 분자 : numerator // 분모 : denominator

    for i in range(M, K-1, -1):
        numerator += combi(M, i)*combi(N-M, M-i)

    denominator = combi(N, M)

    print(numerator/denominator)
