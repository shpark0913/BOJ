N = int(input())  # Nę°ě ě˘í
lst = list(map(int, input().split()))
lst2 = list(set(lst))
lst2.sort()
dic = {}
for i in range(len(lst2)):
    dic[lst2[i]] = i
for elt in lst:
    print(dic[elt], end=' ')
print()