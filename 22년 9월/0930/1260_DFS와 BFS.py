from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
for elt in graph:
    elt.sort()
visited = [0] * (N+1)

def dfs(v):
    visited[v] = 1
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while queue:
        x = queue.popleft()
        print(x, end = ' ')
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

dfs(V)
print()
visited = [0] * (N+1)
bfs(V)