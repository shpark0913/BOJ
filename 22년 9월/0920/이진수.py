def Bbit_print(i):
    output = ""
    for j in range(3, -1, -1):
        output += "1" if i & (1 << j) else "0"
    return output


T = int(input())

for t in range(1, T + 1):
    lst = input().split()
    code = lst[-1]
    digit = ""
    for i in code:
        if i.isdecimal():
            digit += str(Bbit_print(int(i)))
        elif i == 'A':
            digit += '1010'
        elif i == 'B':
            digit += '1011'
        elif i == 'C':
            digit += '1100'
        elif i == 'D':
            digit += '1101'
        elif i == 'E':
            digit += '1110'
        elif i == 'F':
            digit += '1111'
    print(f'#{t}', digit)