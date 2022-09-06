import sys
sys.stdin = open("1094_막대기.txt")

T = int(input())

for t in range(T):
    X = int(input())   # 가지고 싶은 막대 길이
    lst = [64]
    while 1:
        if X != 64:
            if sum(lst) - min(lst)/2 >= X:
                a = min(lst)
                lst.append(a/2)
                lst.remove(a)
            else:
                a = min(lst)
                lst.append(a/2)
                lst.append(a/2)
                lst.remove(a)
            if sum(lst) == X:
                print(len(lst))
                break
        else:
            print(1)
            break