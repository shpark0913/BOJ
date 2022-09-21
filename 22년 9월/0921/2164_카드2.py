import sys
sys.stdin = open("2164_카드2.txt")

N = int(input())
if N == 1:
    print(1)
else:
    for i in range(100):
        if 2**i < N <= 2**(i+1):
            print(2*(N - 2**i))
            break