import sys, math
sys.stdin = open("1064_평행사변형.txt")

T = int(input())

for t in range(T):
    xa, ya, xb, yb, xc, yc = map(int,input().split())
    lst = []
    if xa == xb == xc or ya == yb == yc:
        print(-1.0)

    elif xc != xb and xc != xa and xa != xb and (yc-yb)/(xc-xb) == (yc-ya)/(xc-xa) == (yb-ya)/(xb-xa):
        print(-1.0)

    else:
        alpha_a = xb+xc-xa
        beta_a = yb+yc-ya
        elt_a = 2*math.sqrt((abs(alpha_a - xb))**2 + (abs(beta_a - yb))**2)
        lst.append(elt_a)

        alpha_b = xa+xc-xb
        beta_b = ya+yc-yb
        elt_b = 2*math.sqrt((abs(alpha_b - xc))**2 + (abs(beta_b - yc))**2)
        lst.append(elt_b)

        alpha_c = xa+xb-xc
        beta_c = ya+yb-yc
        elt_c = 2*math.sqrt((abs(alpha_c - xa))**2 + (abs(beta_c - ya))**2)
        lst.append(elt_c)

        print(max(lst)-min(lst))