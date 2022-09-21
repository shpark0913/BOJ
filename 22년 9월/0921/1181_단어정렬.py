import sys
sys.stdin = open("1181_단어정렬.txt")

N = int(input())

lst = {input() for _ in range(N)}
lst = list(lst)
lst.sort()
lst.sort(key=len)       # 길이로 정렬. sort() 1번 또 하면 알파벳 순
for elt in lst:
    print(elt)

# print(lst)
# want_lst = [lst[0]]
# answer = []
# i = 0
#
# while i < len(lst):
#     if len(lst[i]) == len(want_lst[-1]) and lst[i] not in want_lst:
#         want_lst.append(lst[i])
#         i += 1
#     elif len(lst[i]) != len(want_lst[-1]):
#         want_lst.sort()
#         answer = answer + want_lst
#         want_lst = [lst[i]]
#         i += 1
#     elif i == len(lst)-1:
#         want_lst.append(lst[i])
#         want_lst.sort()
#         answer = answer + want_lst
#     else:
#         i += 1
#
# print(answer)
