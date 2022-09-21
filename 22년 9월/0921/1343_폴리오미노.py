import sys
sys.stdin = open("1343_폴리오미노.txt")

T = int(input())

for t in range(T):
    lst = input().split('.')
    poly = []

    for elt in lst:
        if len(elt) % 2:
            poly = [-1]
            break
        elif elt == '':
            poly.append('.')
        elif len(elt) % 4 != 0:
            poly.append('AAAA'*(len(elt)//4) + 'BB')
        else:
            poly.append('AAAA'*(len(elt)//4))

    if poly == [-1]:
        print(-1)
    else:
        for elt in poly[:-1]:
            if elt == '.':
                print(elt, end = '')
            else:
                print(elt+'.', end='')
        if poly[-1] == '.':
            print()
        else:
            print(poly[-1])