import sys
sys.stdin = open("1037_약수.txt")

T = int(input())

# 1번째 풀이
for t in range(T):
    real_div = int(input())              # 진짜 약수들의 개수
    lst = list(map(int,input().split())) # 진짜 약수들
    lst.sort()
    print(lst[0]*lst[-1])

# 2번째 풀이 : list를 정렬하는데 시간이 오래 걸릴 것 같아
#             min, max를 사용했더니 시간이 약간 단축되었다.
for t in range(T):
    real_div = int(input())  # 진짜 약수들의 개수
    lst = list(map(int, input().split()))  # 진짜 약수들
    print(min(lst)*max(lst))