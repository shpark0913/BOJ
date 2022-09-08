import sys
sys.stdin = open("21920_서로소평균.txt")

# import sys
# input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
X = int(input())

divisors_X = []

for i in range(2, X+1):
    if X//i == X/i:         # i가 X의 약수
        divisors_X.append(i)

lst2 = []
for i in divisors_X:
    for elt in lst:
        if elt > i:
            if elt//i == elt/i:
                lst2.append(elt)
        elif elt == i:
            lst2.append(elt)

for elt in lst2:
    if elt in lst:
        lst.remove(elt)

print(sum(lst)//len(lst))