from fractions import Fraction       # 소수가 아니라 분수 표현을 위해 사용

import sys, math                     # denominatior : 분모, numerator : 분자
sys.stdin = open("input.txt")

while 1:
    M, N = map(int,input().split())
    if M == 0:                       # 마지막 input이 0 0 이므로
        break

    Q = Fraction(M, N)               # M/N 으로 시작해서 점점 기약분수들이 차감되는 분수
    lst = []                         # 단위분수들을 원소로 갖는 리스트

    while Q > 0:
        new_deno = math.ceil(1/Q)    # 기약분수의 분모는 원래 분수 역수의 올림값.
        Q1 = Fraction(1, new_deno)
        if (Q - Q1).denominator < 1000000:
            Q -= Q1
            lst.append(Q1)
        else:
            while (Q - Q1).denominator >= 1000000:
                new_deno += 1
                Q1 = Fraction(1, new_deno)
            Q -= Q1
            lst.append(Q1)
    for elt in lst:
        print(elt.denominator, end = ' ')
    print()