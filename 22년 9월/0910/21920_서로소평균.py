import sys, math
sys.stdin = open("21920_서로소평균.txt")

N = int(input())
lst = list(map(int,input().split()))
X = int(input())
c = 0
num = 0
for elt in lst:
    if math.gcd(X, elt) == 1:
        c += elt
        num += 1
    else:
        pass

print(c//num)