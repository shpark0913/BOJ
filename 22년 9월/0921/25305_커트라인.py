import sys
sys.stdin = open("25305_커트라인.txt")

N, k = map(int,input().split())

x = list(map(int,input().split()))
x.sort()
x.reverse()
print(x[k-1])