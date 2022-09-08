import sys
sys.stdin = open("1032_명령프롬프트.txt")

T = int(input())

for t in range(T):
    N = int(input())        # 파일 이름의 개수
    lst = [list(input()) for _ in range(N)]
    new_lst = lst[0]
    if len(lst) == 1:       # 리스트 원소 1개인 경우
        elt = lst[0]
        print(''.join(elt))
    else:
        elt = lst[0]
        for i in range(1, len(lst)):
            for j in range(len(lst[i])):
                if elt[j] != lst[i][j]:
                    elt[j] = '?'
        print(''.join(elt))