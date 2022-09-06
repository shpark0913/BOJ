import sys
sys.stdin = open("11051_이항계수2.txt")


def combi():

    def facto(N):
        c = 1
        for i in range(N, 1, -1):
            c *= i
        return c


    N, K = map(int,input().split())
    const = 1
    for i in range(N, N - K, -1):
        const *= i
    # print(type(const/facto(K)))
    return (const//facto(K))%10007

print(combi())
