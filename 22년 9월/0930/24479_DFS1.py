import sys
sys.setrecursionlimit(100000)

N, M, R = map(int, input().split())

visited = [0] * (N + 1)
graph = [[] for _ in range(N+1)]
lst = []

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for elt in graph:
    elt.sort(reverse=True)

print(graph)
def dfs(v):
    visited[v] = 1
    lst.append(v)
    for i in graph[v]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)

dfs(R)

dic = {}
for i in range(len(lst)):
    dic[lst[i]] = i+1

for i in range(1, N+1):
    if i in dic.keys():
        print(dic[i])
    else:
        print(0)
'''
6 4 1
2 3
1 4
1 5
4 6

'''