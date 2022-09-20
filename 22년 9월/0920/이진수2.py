T = int(input())

for t in range(1, T + 1):
    N = float(input())
    n = 0.5
    digit = "0."
    while N > 0:
        if n <= N:
            digit += "1"
            N -= n
            n /= 2
        else:
            digit += "0"
            n /= 2
    digit_new = digit[2:]
    if len(digit_new) >= 13:
        print(f'#{t} overflow')
    else:
        print(f'#{t} {digit_new}')