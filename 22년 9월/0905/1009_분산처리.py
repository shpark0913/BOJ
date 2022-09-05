import sys
sys.stdin = open("1009_분산처리.txt")

T = int(input())
for t in range(T):
    a, b = map(int,input().split())
    c = a
    for _ in range(b-1):
        c = (c%10)*a
    c = c%10
    if c == 0:
        print(10)
    else:
        print(c)

# for t in range(T):
#     a, b = map(int,input().split())
#     c = a**b % 10
#     if c == 0:
#         print(10)
#     else:
#         print(c)
'''
주석처리한 코드는 처음 짠 코드입니다.
그런데 b가 커지면 a**b 의 계산에 시간이 너무 소요돼서 시간 초과가 뜹니다.
그래서 생각한 방법이 1의 자리만 중요하기에 계산 과정에서 계속 10을 나눠서
1의 자리에만 집중을 하는 코드를 구상했고 통과했습니다:)
'''
